#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prd_moc_supervisor.py — N243 Supervisor avec narration TALEX.

Rôle :
- Recevoir les verdicts VERSES
- Appliquer la logique ternaire (APPROUVER/SUSPENDRE/REJETER)
- Enrichir les verdicts via TALEX governance adapters
- Générer une narrative de supervision
- Enregistrer dans le WAL ternaire
- Publier sur WAZAA bus
- Tracer dans KG-L
- Synchroniser OBS
- Valider le frontmatter des PRD/MOC (NOUVEAU S3.1)
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

# TALEX governance adapters
try:
    from talex.governance import GovernanceReader
    from talex.core.unified_graph import UnifiedSemanticGraph
    TALEX_AVAILABLE = True
except ImportError:
    TALEX_AVAILABLE = False

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


# ── Chemins ──────────────────────────────────────────────────────────────

VOLTX_ROOT = Path(r"D:\DO\WEB\TOOLS\L0-CANON\VOLTX")
N243_ROOT = Path(r"D:\DO\WEB\TOOLS\L4-TOOLS\N243")
KG_L_ANCHOR = N243_ROOT / "kilocode" / "semantics" / "anchor.py"
OBS_VAULT = VOLTX_ROOT
WAZAA_BUS = VOLTX_ROOT / "PLATFORM" / "scripts" / "platform" / "wazaa_bus.py"


# ── WAL Ternaire ─────────────────────────────────────────────────────────


class TernaryWAL:
    """Write-Ahead Log ternaire pour N243."""

    def __init__(self, wal_path: Path) -> None:
        self.wal_path = wal_path
        self.wal_path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, verdict: str, repo: str, details: Dict[str, Any]) -> None:
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "verdict": verdict,
            "repo": repo,
            "details": details,
        }
        with self.wal_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def read_last(self, n: int = 10) -> list[dict]:
        if not self.wal_path.exists():
            return []
        lines = self.wal_path.read_text(encoding="utf-8").strip().splitlines()
        entries = []
        for line in lines[-n:]:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except Exception:
                pass
        return entries


# ── N243 Supervisor ──────────────────────────────────────────────────────


class N243Supervisor:
    """Superviseur N243 avec enrichissement TALEX."""

    def __init__(self, wal_path: Optional[Path] = None) -> None:
        self.wal = TernaryWAL(wal_path or N243_ROOT / "WAL" / "ternary-wal.jsonl")
        self.graph: Optional[UnifiedSemanticGraph] = None
        if TALEX_AVAILABLE:
            reader = GovernanceReader(
                voltx_root=VOLTX_ROOT,
                mox_wrapper=VOLTX_ROOT / "L2-PLATFORM" / "MOX" / "src" / "cli" / "mox_governance_wrapper.py",
                verses_consensus=VOLTX_ROOT / "PLATFORM" / "scripts" / "platform" / "holographic_consciousness.py",
                n243_supervisor=N243_ROOT / "agents" / "prd_moc_supervisor.md",
                kg_l_anchor=KG_L_ANCHOR,
                obs_vault=OBS_VAULT,
            )
            self.graph = UnifiedSemanticGraph()
            reader.read(self.graph)

    def _talex_context(self) -> Dict[str, Any]:
        """Extrait un contexte narratif depuis le graphe TALEX."""
        if not self.graph:
            return {}
        context: Dict[str, Any] = {
            "nodes": [],
            "edges": [],
        }
        for node_id, node in self.graph.nodes.items():
            context["nodes"].append({
                "id": node_id,
                "label": node.label,
                "kind": node.kind.value,
                "repo": node.repo,
                "status": node.status,
                "meta": node.meta,
            })
        for edge in self.graph.edges:
            context["edges"].append({
                "source": edge.source,
                "target": edge.target,
                "kind": edge.kind.value,
                "weight": edge.weight,
                "meta": edge.meta,
            })
        return context

    def supervise(self, repo: str, verdict: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Applique la logique ternaire et enregistre le verdict."""
        payload = payload or {}
        talex_context = self._talex_context()

        decision = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "repo": repo,
            "verdict": verdict,
            "payload": payload,
            "talex_context": talex_context,
        }

        # Logique métier
        if verdict == "APPROUVER":
            decision["action"] = "execute"
            decision["message"] = "Action approuvée et exécutée"
        elif verdict == "SUSPENDRE":
            decision["action"] = "pending"
            decision["message"] = "Action suspendue, notification OBS envoyée"
        elif verdict == "REJETER":
            decision["action"] = "archive"
            decision["message"] = "Action rejetée et archivée"
        else:
            decision["action"] = "unknown"
            decision["message"] = f"Verdict inconnu: {verdict}"

        self.wal.append(verdict, repo, decision)
        self._publish_wazaa(decision)
        self._trace_kg_l(decision)
        self._sync_obs(decision)
        return decision

    def last_decisions(self, n: int = 10) -> list[dict]:
        """Retourne les N derniers verdicts."""
        return self.wal.read_last(n)

    def narrative(self) -> str:
        """Génère une narrative de supervision via TALEX."""
        decisions = self.last_decisions()
        lines = [
            "# N243 Supervision Narrative",
            "",
            f"Generated: {datetime.now(timezone.utc).isoformat()}",
            "",
            "## Recent Decisions",
            "",
        ]
        for decision in decisions:
            lines.append(f"- {decision['timestamp']} — `{decision['verdict']}` — {decision['repo']}")
        lines.append("")
        return "\n".join(lines)

    def _publish_wazaa(self, decision: Dict[str, Any]) -> None:
        """Publie le verdict sur WAZAA bus si disponible."""
        if not WAZAA_BUS.exists():
            return
        try:
            subprocess.run(
                [
                    sys.executable,
                    str(WAZAA_BUS),
                    "publish",
                    "prd_moc.gate",
                    json.dumps(decision, ensure_ascii=False),
                ],
                capture_output=True,
                timeout=30,
            )
        except Exception:
            pass

    def _trace_kg_l(self, decision: Dict[str, Any]) -> None:
        """Trace la décision dans KG-L si disponible."""
        if not KG_L_ANCHOR.exists():
            return
        try:
            subprocess.run(
                [
                    sys.executable,
                    str(KG_L_ANCHOR),
                    "trace",
                    "execution_trace",
                    json.dumps(decision, ensure_ascii=False),
                ],
                capture_output=True,
                timeout=30,
            )
        except Exception:
            pass

    def _sync_obs(self, decision: Dict[str, Any]) -> None:
        """Synchronise l'état dans OBS si disponible."""
        if not OBS_VAULT.exists():
            return
        try:
            subprocess.run(
                [
                    sys.executable,
                    str(OBS_VAULT / "06_Bridges" / "sync_obsidian_to_repos.py"),
                    "--status",
                    decision["verdict"].lower(),
                ],
                capture_output=True,
                timeout=30,
            )
        except Exception:
            pass

    def validate_frontmatter(self, path: Path) -> Dict[str, Any]:
        """Valide le frontmatter YAML d'un PRD/MOC.

        Retourne un verdict APPROUVER/SUSPENDRE/REJETER selon la conformité.
        """
        result: Dict[str, Any] = {
            "path": str(path),
            "valid": False,
            "verdict": "REJETER",
            "errors": [],
        }

        if not YAML_AVAILABLE:
            result["errors"].append("PyYAML not available")
            return result

        if not path.exists():
            result["errors"].append(f"File not found: {path}")
            return result

        content = path.read_text(encoding="utf-8")
        match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not match:
            result["errors"].append("Missing YAML frontmatter block")
            return result

        try:
            frontmatter = yaml.safe_load(match.group(1)) or {}
        except Exception as exc:
            result["errors"].append(f"Invalid YAML: {exc}")
            return result

        required_fields = ["type", "version", "date", "status", "intent_hash"]
        missing = [field for field in required_fields if field not in frontmatter]
        if missing:
            result["errors"].append(f"Missing required fields: {missing}")
            return result

        allowed_types = {"PRD", "PRD-MOC", "EPIC", "ADR", "SPEC", "INTENT"}
        doc_type = str(frontmatter.get("type", ""))
        if doc_type not in allowed_types:
            result["errors"].append(f"Invalid type: {doc_type}")
            return result

        allowed_statuses = {
            "PRD": {"draft", "active", "deprecated", "superseded"},
            "PRD-MOC": {"draft", "proposed", "approved", "active", "deprecated", "superseded"},
            "EPIC": {"draft", "active", "done", "deprecated", "superseded"},
            "ADR": {"proposed", "accepted", "deprecated", "superseded"},
            "SPEC": {"draft", "stable", "deprecated", "superseded"},
            "INTENT": {"draft", "proposed", "active", "deprecated", "superseded"},
        }
        status = str(frontmatter.get("status", ""))
        if status not in allowed_statuses.get(doc_type, set()):
            result["errors"].append(f"Invalid status '{status}' for type '{doc_type}'")
            return result

        if not re.search(r"^0x[A-Z0-9_]+$", str(frontmatter.get("intent_hash", ""))):
            result["errors"].append("Invalid intent_hash format")
            return result

        result["valid"] = True
        result["verdict"] = "APPROUVER"
        result["frontmatter"] = frontmatter
        return result


# ── CLI ──────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description="N243 Supervisor with TALEX governance")
    parser.add_argument("--repo", help="Repo cible")
    parser.add_argument("--verdict", choices=["APPROUVER", "SUSPENDRE", "REJETER"])
    parser.add_argument("--payload", default="{}", help="Payload JSON")
    parser.add_argument("--wal", default=str(N243_ROOT / "WAL" / "ternary-wal.jsonl"))
    parser.add_argument("--last", type=int, default=0, help="Afficher les N derniers verdicts")
    parser.add_argument("--narrative", action="store_true", help="Générer la narrative de supervision")
    args = parser.parse_args()

    if not args.narrative and not args.last:
        if not args.repo or not args.verdict:
            parser.error("--repo et --verdict sont requis sauf avec --narrative ou --last")

    supervisor = N243Supervisor(wal_path=Path(args.wal))

    if args.last > 0:
        for decision in supervisor.last_decisions(args.last):
            print(json.dumps(decision, ensure_ascii=False))
        return 0

    if args.narrative:
        print(supervisor.narrative())
        return 0

    payload = json.loads(args.payload)
    decision = supervisor.supervise(args.repo, args.verdict, payload)
    print(json.dumps(decision, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
