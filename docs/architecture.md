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
├── schemas/                  ← PRD-001 : kinds Nostr personnalisés
├── agents/                   ← PRD-002 : protocole runner
├── workflows/                ← PRD-003 : actions ternaires
├── wal/                      ← PRD-004 : WAL ternaire
├── bdcp/                     ← PRD-005 : enforcement BDCP
├── patches/                  ← Patches historiques supersedés (pivot WAZAA)
├── src/                      ← Code Rust placeholder
├── docs/                     ← Documentation
├── tests/                    ← Tests
├── STRATUM_RELAY.md          ← Gouvernance L4
├── REPO.yaml                 ← Identité RSS-v2
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

1. Définit les schémas d'événements Nostr personnalisés (kinds 40050-40057)
2. Pilote les runners Zig via ACP/subprocess (RunnerAdapter)
3. Implémente les actions ternaires Approve/Suspend/Reject
4. Trace l'état Convergence/Divergence/Oscillation dans un WAL
5. Valide les clones via BDCPChecker contre `known_repositories.yaml`

---

## Relation WAZAA ↔ N243

```
WAZAA (bus orchestration, port 1873)
    ↑
    │ unités Intent / événements
    │
N243 (meta-orchestrateur)
    │
    ├── schemas/kinds-lstar.md → kinds 40050-40057
    ├── agents/runner-protocol.md → RunnerAdapter
    ├── workflows/ternary-actions.md → TernaryAction
    ├── wal/ternary-wal.md → TernaryWAL (+ wal_event_emitter.py)
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
