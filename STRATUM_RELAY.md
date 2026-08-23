---
relay_version: 7
repo: gerivdb/N243
strate: L4
lifecycle: PROPOSED
vague: 1
synchro: '2026-07-31'
hub: gerivdb/GOVERNANCE-HUB
intent_hash: '0xN243_20260801'
stratum_relay: STRATUM_RELAY.md
rss_compliance:
  version: v2.3
  profile: CITIZEN
  score: 11/11
  status: CONFORME
  last_audit: '2026-07-31'
rules:
  - id: R1
    assertion: >-
      N243 n'est PAS un fork Git de WAZAA.
      C'est un meta-orchestrateur cognitif qui pilote les runners Zig via le bus WAZAA et un WAL ternaire.
      Posture : couche N+3 d'orchestration, pas duplication de code.
    status: VERIFIED
    severity: MEDIUM
    decision_date: '2026-07-31'
  - id: R2
    assertion: Toute décision d'impact transverse doit être backing par un ADR avant implémentation.
    status: VERIFIED
    severity: HIGH
  - id: R3
    assertion: Les patches historiques Buzz@block sont SUPERSEDES (pivot WAZAA 2026-08-23) et conservés dans N243/patches/.
    status: VERIFIED
    severity: MEDIUM
---

# STRATUM RELAY — N243 (L4)

**VAGUE**: 1 | **Synchro**: 2026-07-31 | **Hub**: gerivdb/GOVERNANCE-HUB

---

## Identité stratique

- **Strate** : `L4-TOOLS` — Extensions & Intégrations
- **Role canonique** : Meta-orchestrateur cognitif L* qui pilote les runners Zig via le bus WAZAA, WAL ternaire et protocole BDCP
- **Posture** : Couche N+3 d'orchestration — pas duplication de code, orchestration par événements
- **Parent** : L3
- **Enfants** : L5

---

## Navigation rapide

- PRD canonique : `GOVERNANCE-HUB/PRD/PRD_N243_ORCHESTRATOR.md`
- Substrat cognitif : `gerivdb/LLM-REPO` (L1b — privé)
- Standards repo : `REPO-STANDARDS-L4.md`
- Transit map : `VERSUS/urban_ontology_verse/TRANSIT/transit_map.yaml`

---

## Architecture

N243 **n'est pas un fork** de WAZAA. C'est un **meta-orchestrateur** qui :

- Définit les schémas d'événements Nostr personnalisés (kinds 40050-40057)
- Pilote les runners Zig via ACP/subprocess (RunnerAdapter)
- Implémente les actions ternaires Approve/Suspend/Reject
- Trace l'état Convergence/Divergence/Oscillation dans un WAL
- Valide les clones via BDCPChecker contre `known_repositories.yaml`

---

## Composants N243

| Composant | Localisation | Description |
|---|---|---|
| PRD-001 | schemas/kinds-lstar.md | Nouveaux kinds 40050-40057 |
| PRD-002 | agents/runner-protocol.md (bus WAZAA) | RunnerAdapter pour runners Zig |
| PRD-003 | workflows/ternary-actions.md | TernaryAction + TernaryActionConfig |
| PRD-004 | wal/ternary-wal.md (+ WAZAA wal_event_emitter.py) | TernaryState + TernaryWAL |
| PRD-005 | bdcp/enforcer.md (src/bdcp.rs) | BDCPChecker pour validation clones |

---

## Conformite RSS-v2.3

| Exigence CITIZEN | Statut |
|---|---|
| `README.md` | ✅ |
| `.gitignore` | ✅ |
| `.rssignore` | ✅ |
| `REPO.yaml` | ✅ |
| `citizens.yaml` | ✅ |
| `ONTOLOGY_DECLARATION.yaml` | ✅ |
| `docs/` | ✅ |
| `src/` | ✅ |
| `config/` | ✅ |
| `tests/` | ✅ |
| `.github/` | ✅ |
| **Score** | **11/11** |

---

## Dependances directes

**Parents (amont)** :
- gerivdb/WAZAA
- gerivdb/BRAIN-DOCS
- gerivdb/SKILLS

**Enfants (aval)** :
- Aucun pour l'instant (proposed)

---

## Vague de mise a jour

| Vague | Contenu | Statut |
|---|---|---|
| **1 (courante)** | Scaffolding N243, intégration WAZAA (pivot Buzz@block), PRD-001 à PRD-005 | En cours |

---

*Mise a jour manuelle 2026-07-31 — session N243 Phase 1*
