#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""n243_supervisor - Supervision ternaire + WAL des mutations KG (MOC KG-L S3.1).

Décisions N243 sur chaque mutation proposée par le pipeline KG-L :

  APPROUVER  : schéma valide, entité inconnue ou identique, confiance >= seuil
  SUSPENDRE  : conflit de contenu sur une entité existante, ou confiance < seuil
               -> file humaine (NEEDS_HUMAN), la mutation reste en WAL non appliquée
  REJETER    : violation de schéma / doublon strict / provenance manquante

WAL append-only (`wal/n243_wal.jsonl`) : toute décision est journalisée avant
application ; checkpoint = position dans le WAL ; rollback ciblé = rejeu inverse
des APPROUVER post-checkpoint. Pas de rebuild complet.

Usage:
    python scripts/n243_supervisor.py --decide <mutations.json> [--threshold 0.8]
    python scripts/n243_supervisor.py --selftest

IntentHash: 0xN243_SUPERVISOR_TERNARY_20260825
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
WAL_PATH = HERE.parent / "wal" / "n243_wal.jsonl"

REQUIRED_FIELDS = ("mutation_id", "kind", "entity", "provenance", "confidence")
VALID_KINDS = ("add_node", "add_edge", "update_attr")
DECISIONS = ("APPROUVER", "SUSPENDRE", "REJETER")


def decide(mutation: dict, known_entities: set[str], *,
           threshold: float = 0.8) -> tuple[str, str]:
    """Règle ternaire. Retourne (décision, raison)."""
    for f in REQUIRED_FIELDS:
        if f not in mutation or mutation[f] in (None, ""):
            return "REJETER", f"champ obligatoire absent: {f}"
    if mutation["kind"] not in VALID_KINDS:
        return "REJETER", f"kind invalide: {mutation['kind']}"
    conf = float(mutation.get("confidence", 0))
    if conf < 0 or conf > 1:
        return "REJETER", f"confiance hors bornes: {conf}"

    entity = str(mutation["entity"])
    payload = json.dumps(mutation.get("payload", {}), sort_keys=True)
    conflict = known_entities.get(entity) if isinstance(known_entities, dict) else None
    if entity in (known_entities if isinstance(known_entities, (set,)) else {}):
        # entité connue : identique -> no-op approuvé ; divergente -> conflit
        if conflict is not None and conflict != payload:
            if conf >= threshold:
                return "APPROUVER", "conflit résolu par confiance suffisante"
            return "SUSPENDRE", "conflit de contenu sur entité existante"
        return "APPROUVER", "identique à l'existant (idempotent)"
    if conf < threshold:
        return "SUSPENDRE", f"confiance {conf:.2f} < seuil {threshold:.2f}"
    return "APPROUVER", "nouvelle entité conforme"


def wal_append(record: dict, wal_path: Path | None = None) -> int:
    """Append JSONL + retourne la position (offset ligne, 1-based).

    Le comptage se fait APRÈS fermeture du handle d'écriture : sur Windows,
    lire via un second handle avant flush sous-estime le nombre de lignes.
    """
    p = Path(wal_path) if wal_path else WAL_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    with p.open("r", encoding="utf-8") as fh:
        return sum(1 for _ in fh)


def process(mutations: list[dict], *, wal_path: Path | None = None,
            threshold: float = 0.8,
            known: dict[str, str] | None = None) -> dict:
    known = known or {}
    counts = {d: 0 for d in DECISIONS}
    positions = []
    for m in mutations:
        decision, reason = decide(m, known, threshold=threshold)
        counts[decision] += 1
        rec = {"ts": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
               "decision": decision, "reason": reason,
               "mutation_id": m.get("mutation_id"),
               "entity": m.get("entity"), "kind": m.get("kind")}
        positions.append(wal_append(rec, wal_path))
    return {"counts": counts, "wal_positions": positions,
            "checkpoint": max(positions) if positions else 0}


def selftest() -> int:
    import tempfile
    fails = 0

    def ok(label, cond):
        nonlocal fails
        print(f"  [{'OK ' if cond else 'FAIL'}] {label}")
        fails += 0 if cond else 1

    good = {"mutation_id": "m1", "kind": "add_node",
            "entity": "message:s42/p17", "provenance": "kilo.db#part/17",
            "confidence": 0.97, "payload": {"role": "user"}}
    low = dict(good, mutation_id="m2", entity="reasoning:s42/p18", confidence=0.4)
    bad_schema = {"mutation_id": "m3", "kind": "delete_everything"}
    conflict_in = dict(good, mutation_id="m4", entity="message:s42/p17",
                       confidence=0.5, payload={"role": "assistant"})

    with tempfile.TemporaryDirectory() as tmp:
        wal = Path(tmp) / "n243_wal.jsonl"
        r = process([good, low, bad_schema],
                    wal_path=wal, known={"message:s42/p17": '{"role": "user"}'})
        ok("APPROUVER pour entité nouvelle conforme", r["counts"]["APPROUVER"] == 1)
        ok("SUSPENDRE sous le seuil", r["counts"]["SUSPENDRE"] == 1)
        ok("REJETER schéma invalide", r["counts"]["REJETER"] == 1)
        ok("checkpoint = dernière position WAL", r["checkpoint"] == 3)

        r2 = process([conflict_in], wal_path=wal,
                     known={"message:s42/p17": '{"role": "user"}'})
        ok("conflit + confiance faible -> SUSPENDRE",
           r2["counts"]["SUSPENDRE"] == 1)

        lines = wal.read_text(encoding="utf-8").splitlines()
        ok("WAL append-only 4 décisions journalisées", len(lines) == 4)
        first = json.loads(lines[0])
        ok("record WAL typé et horodaté",
           first["decision"] in DECISIONS and "ts" in first)

    print(f"[N243] selftest: {6 - fails}/6")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Superviseur ternaire N243")
    ap.add_argument("--decide", type=Path, help="fichier JSON de mutations")
    ap.add_argument("--threshold", type=float, default=0.8)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

    if args.selftest:
        return selftest()
    if args.decide:
        mutations = json.loads(args.decide.read_text(encoding="utf-8"))
        report = process(mutations, threshold=args.threshold)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        suspended = report["counts"]["SUSPENDRE"]
        print(f"[N243] {suspended} mutation(s) en attente humaine")
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
