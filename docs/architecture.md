# Architecture — N243

**Dernière mise à jour :** 2026-07-31  
**Strate :** L4 — Interfaces utilisateur & Dev  
**Référence :** `STRATUM_RELAY.md` | `REPO.yaml`

---

## Posture

N243 est un **meta-orchestrateur cognitif L4** sur WAZAA — une couche d'orchestration
qui pilote les runners via le bus WAZAA sans embarquer de code WAZAA.

- Pas un fork Git de `WAZAA`
- Pas de code WAZAA embarqué
- Orchestration par événements (unités Intent) signés
- Exécution déléguée aux runners Zig via l'adaptateur N243/subprocess

---

## Structure

```
N243/
├── PRD/                      ← PRD-001 : gate orchestration & runner protocol
├── src/
│   └── gates/                ← L5/L6 gates, memory gate, runner protocol
├── agents/                   ← Supervisor PRD/MOC autonome
├── wal/                      ← WAL ternaire (replay + compact TTL 30j)
├── bdcp/                     ← Enforcement BDCP
├── patches/                  ← Patches historiques supersedés (pivot WAZAA)
├── docs/                     ← Documentation
├── tests/                    ← Tests Rust + Python
├── STRATUM_RELAY.md          ← Gouvernance L4
├── REPO.yaml                 ← Identité RSS-v2
├── ONTOLOGY_DECLARATION.yaml ← Ontologie N243
├── design.yaml               ← Configuration conception
└── Cargo.toml                ← Dépendances Rust pures (orchestration via bus WAZAA)
```

---

## Dépendances

- **Upstream :** WAZAA, BRAIN-DOCS, SKILLS  
  (fournissent bus d'orchestration, documentation, compétences)

- **Downstream :** Aucun pour l'instant (proposed)

- **Runtime cible :** bus WAZAA (unités Intent) — port 1873

---

## Fonctionnement

N243 agit comme un **méta-orchestrateur** qui :

1. Orchestre les gates ternaires L5/L6 via `src/gates/`
2. Pilote les runners L* (LLUX, RLM-243, TIMX, ROOTX, TLM-CORE) via `runner_protocol.rs`
3. Trace les décisions APPROUVER/SUSPENDRE/REJETER dans un WAL ternaire (`src/wal.rs`)
4. Valide les documents de gouvernance PRD/MOC via `agents/prd_moc_supervisor.py`
5. Publie les verdicts sur le bus WAZAA topic `prd_moc.gate`

---

## Relation WAZAA ↔ N243

```
WAZAA (bus orchestration, port 1873)
    ↑
    │ unités Intent / événements
    │
N243 (meta-orchestrateur)
    │
    ├── src/gates/l5.rs → Gate domaine (APPROUVER/SUSPENDRE/REJETER)
    ├── src/gates/l6.rs → Gate runner (Ed25519 proof)
    ├── src/gates/memory_gate.rs → Gate mémoire (écritures)
    ├── src/gates/runner_protocol.rs → Protocole runners L* (KEEL R9)
    ├── agents/prd_moc_supervisor.py → Validation PRD/MOC + WAZAA publish
    ├── wal/ternary-wal.md → WAL ternaire (replay + compact TTL 30j)
    └── bdcp/enforcer.md → BDCPChecker (src/bdcp.rs)
```

---

## Pivot Buzz@block → WAZAA

L'ancienne base Buzz@block est abandonnée dans ENV2 (décision 2026-08-23) :

| Élément historique (Buzz@block) | Équivalent N243 / WAZAA |
|---|---|
| Relay/bloc Buzz@block | Bus WAZAA + meta-orchestrateur N243 |
| API Nostr/NIP-34 | Unités Intent + runners Zig |
| buzz-ecos-integration | n243-orchestrator (via WAZAA) |
| KiloCode (VS Code) | WAZAA (bus événements) |
| Extension overlay | Orchestration cognitive |
