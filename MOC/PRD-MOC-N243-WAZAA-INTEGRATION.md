---
type: PRD-MOC
version: "1.0.0"
date: "2026-09-17"
status: accepted
intent_hash: 0xPRD_MOC_N243_WAZAA_INTEGRATION_20260917
author: gerivdb
source_repo: gerivdb/N243
source_path: MOC/PRD-MOC-N243-WAZAA-INTEGRATION.md
parent_doc: PRD-MOC-N243-MASTER.md
related_adr: ADR-2026-06-28-001-LOGICAL-ARCHITECTURE-N1-N4.md, ADR-2026-07-28-019-INTENT-VALIDATION-PIPELINE.md, ADR-2026-07-28-020-CTULU-TRIX-ECOS-CLI-ORCHESTRATION.md
related_intent: INTENT-Q243-NATIVE-INFERENCE-20260825
related_moc: PRD-MOC-N243-MASTER.md, PRD-MOC-WAZAA-MASTER.md, PRD-MOC-N243-ORCHESTRATOR.md
---

# PRD-MOC — N243 WAZAA Integration

> **Scope** : Intégration entre N243 (`gerivdb/N243`) et WAZAA (`gerivdb/WAZAA`).
> **Statut** : proposed — en attente de validation HITL et review cross-repo.

## 1. RÉSUMÉ EXÉCUTIF

WAZAA est le bus événementiel Intent, WAL et EventServer utilisé par N243 pour
l'orchestration des runners cognitifs (LLUX, RLM-243, TIMX, ROOTX, TLM-CORE).

Ce MOC documente les points d'intégration, les contrats et l'état opérationnel.

## 2. CONTRATS D'INTÉGRATION

| Composant N243 | Composant WAZAA | Protocole |
|---|---|---|
| `WazaaBridge` | Bus Intent | publish/subscribe |
| `N243WAL` | WAL append-only | fichier JSONL |
| `WalEmitter` | Émission WAL | append-only |
| `workflows` | Workflow engine | YAML + EventServer |

## 3. ARCHITECTURE

```
N243                              WAZAA
├── src/bridge/wazaa_bridge.rs ──► Bus Intent
├── src/wal.rs           ──► WAL append-only
├── src/wal_emitter.rs   ──► Émission WAL
├── src/workflows.rs     ──► Workflow engine
└── src/orchestrator.rs  ──► Coordination
```

## 4. POINTS D'ENTRÉE OPÉRATIONNELS

| Opération | Commande | Référence |
|---|---|---|
| **Build** | `cargo build` | `README.md` |
| **Run** | `cargo run` | `README.md` |
| **WAL** | `wal/ternary-wal.md` | PRD-004 |
| **BDCP** | `bdcp/enforcer.md` | PRD-005 |

## 5. CRITÈRES D'ACCEPTATION

| Critère | Validation |
|---------|------------|
| WazaaBridge compile | `cargo check` PASS |
| WAL append-only compile | `cargo check` PASS |
| Tests WAZAA passent | `cargo test` PASS |
| WAZAA repo présent | `D:/DO/WEB/TOOLS/L4-TOOLS/WAZAA` exists |

## 6. ÉTAT OBSERVÉ

**2026-09-17T05:29+02:00** — Proof-of-Life auto-mode SLM :
- [x] `WazaaBridge` connect/publish/subscribe implémenté
- [x] `N243WAL` replay/compact/compact_ttl implémenté
- [x] `WalEmitter` émission convergence/divergence/oscillation implémenté
- [x] `cargo test` PASS
- [x] WAZAA repo présent

### Preuves d'exécution horodatées

```
[RUST] cargo test -- 2026-09-17T05:29+02:00
  test result: ok. 40 passed; 0 failed; 0 ignored; 0 measured

[GIT] git push origin main -- 2026-09-17T05:29+02:00
  To https://github.com/gerivdb/N243.git
  defeb74..ce51e0e  main -> main
```

## 7. DÉPENDANCES CROSS-REPO

| Dépendance | Repo | Rôle | Statut |
|---|---|---|---|
| WAZAA | `L4-TOOLS/WAZAA` | Bus événementiel Intent, WAL, EventServer | ✅ Présent |
| N243 | `L4-TOOLS/N243` | Orchestrateur cognitif | ✅ Présent |

## 8. RISQUES ET MITIGATIONS

| Risque | Description | Mitigation |
|---|---|---|
| Dépendance WAZAA | WAZAA doit être stable | CI WAZAA + tests intégration |
| BDCP | Mode BDCP obligatoire | `bdcp/enforcer.md` documenté |

## 9. RÉFÉRENCES

- **MASTER** : `PRD-MOC-N243-MASTER.md`
- **MOC WAZAA** : `PRD-MOC-WAZAA-MASTER.md`
- **MOC Orchestrator** : `PRD-MOC-N243-ORCHESTRATOR.md`
- **ADR** : ADR-2026-06-28-001-LOGICAL-ARCHITECTURE-N1-N4
- **IntentHash** : 0xN243_META_ORCHESTRATOR_20260801
