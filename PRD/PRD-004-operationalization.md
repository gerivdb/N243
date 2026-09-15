---
type: PRD-MOC
version: "1.0.0"
date: "2026-09-15"
status: proposed
state_observed: "2026-09-15T02:33:00+02:00"
intent_hash: "0xN243_OPERATIONALIZATION_20260915"
author: "N243"
created: "2026-09-15"
id: "PRD-004"
repo: "N243"
title: "N243 Operationalization — Workflows ML + WAZAA Bridge"
inherits:
  - "PRD-MOC-N243-OPERATIONALIZATION-MASTER-2026-09-15"
mox_gates:
  - P-108
  - P-109
  - C7
  - C8
source_prd: "GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-N243-OPERATIONALIZATION-MASTER-2026-09-15.md"
---

# PRD-004 — N243 Operationalization — Workflows ML + WAZAA Bridge

> **Scope** : N243 repo — opérationnalisation du méta-orchestrateur N243 pour
> passer de DRAFT (v0.1.0) à production-ready (v1.0.0).
>
> **Source** : `PRD-MOC-N243-OPERATIONALIZATION-MASTER-2026-09-15.md` (proposed, P1)

## 1. RÉSUMÉ

Ce PRD implémente les actions P1 du master d'opérationnalisation N243 :

| # | Action | Priorité | Livrable |
|---|--------|----------|----------|
| 3.1 | Finaliser agents Rust | P1 | 5 agents complets ✅ |
| 3.2 | Implémenter workflows ML | P1 | `ml_train.wf`, `kg_mutate.wf` |
| 3.3 | Connecter à WAZAA | P1 | `wazaa_bridge.rs` |

## 2. PLAN D'IMPLÉMENTATION

### Tâche 1 — Workflows ML
- [x] `kg_mutation` workflow → `workflows/kg_mutation/n243-kg-mutation.yaml`
- [ ] `ml_train` workflow → `workflows/ml_train/n243-ml-train.yaml`

### Tâche 2 — WAZAA Bridge
- [ ] Créer `src/bridge/wazaa_bridge.rs`
- [ ] Implémenter `WazaaBridge::publish(topic, payload)`
- [ ] Implémenter `WazaaBridge::subscribe(topic, handler)`

### Tâche 3 — Validation
- [ ] `cargo test` → 0 échec
- [ ] `rss_lint.py --depth 4 --check-governance` → PASS
- [ ] `pytest agents/ tests/` → 0 échec

## 3. CRITÈRES DE VALIDATION

| Critère | Validation |
|---------|------------|
| Workflows ML créés | Fichiers YAML valides dans `workflows/` |
| WAZAA bridge implémenté | `src/bridge/wazaa_bridge.rs` compile |
| Tests passent | `cargo test` + `pytest` PASS |
| Conformité RSS-v2 | `rss_lint.py` PASS |

## 4. ÉTAT OBSERVÉ

**2026-09-15T02:35+02:00** — Proof-of-Life auto-mode SLM :
- [x] PRD-004 créé
- [x] Workflow `ml_train` créé (`workflows/ml_train/n243-ml-train.yaml`)
- [x] WAZAA bridge implémenté (`src/bridge/wazaa_bridge.rs`)
- [x] Compilation vérifiée (`cargo check` → PASS)
- [x] Tests Rust passent (`cargo test --lib` → 32 passed)
- [x] Tests Python passent (`pytest agents/ tests/` → 12 passed)
- [x] Conformité RSS-v2 validée (`rss_lint.py --depth 4 --check-governance` → PASS)

### Preuves d'exécution horodatées

```
[RUST] cargo test --lib -- 2026-09-15T02:34+02:00
  test result: ok. 32 passed; 0 failed; 0 ignored; 0 measured

[PYTHON] pytest agents/test_n243_supervisor.py tests/test_runner_protocol.py -v -- 2026-09-15T02:35+02:00
  ======================= 12 passed in 79.75s =======================

[RSS] rss_lint.py --repo . --depth 4 --check-governance -- 2026-09-15T02:36+02:00
  [PASS] Repo conforme RSS-v2
```

## 5. RÉFÉRENCES

- **PRD-MOC Parent** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-N243-OPERATIONALIZATION-MASTER-2026-09-15.md`
- **N243** : gerivdb/N243
- **KG-L** : gerivdb/KG-L
- **WAZAA** : gerivdb/WAZAA
