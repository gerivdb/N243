---
type: PRD-MOC
version: "1.0.0"
date: "2026-09-17"
status: accepted
state_observed: "2026-09-15T02:48:00+02:00"
intent_hash: "0xN243_ML_TRAINING_PIPELINE_20260915"
author: "N243"
created: "2026-09-15"
id: "PRD-006"
repo: "N243"
title: "N243 ML Training Pipeline — Orchestration Rust"
inherits:
  - "PRD-MOC-KG-L-ML-TRAINING-PIPELINE-2026-09-15"
mox_gates:
  - P-108
  - P-109
  - C7
  - C8
source_prd: "GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-KG-L-ML-TRAINING-PIPELINE-2026-09-15.md"
---

# PRD-006 — N243 ML Training Pipeline — Orchestration Rust

> **Scope** : N243 repo — orchestration Rust du pipeline ML training.
> Les modèles Python (GNN, Transformer) restent dans KG-L.
> N243 fournit l'orchestrateur, le WAL, la supervision ternaire et l'intégration VOLTX/WAZAA.
>
> **Source** : `PRD-MOC-KG-L-ML-TRAINING-PIPELINE-2026-09-15.md` (proposed, P1)

## 1. RÉSUMÉ

Orchestration Rust du pipeline ML training dans N243 :

| Composant N243 | Description | Fichier |
|----------------|-------------|---------|
| `ml_train` workflow | Pipeline entraînement ML | `workflows/ml_train/n243-ml-train.yaml` |
| `kg_mutation` workflow | Mutation KG-L | `workflows/kg_mutation/n243-kg-mutation.yaml` |
| `WAZAA bridge` | Publication/ souscription bus | `src/bridge/wazaa_bridge.rs` |
| `VOLTX bridge` | 5 canaux intégrés | `src/bridge/voltx_bridge.rs` |
| Agents KG-L | LluxAgent, TimxAgent, RootxAgent, TlmAgent | `src/agents.rs` |

## 2. INTÉGRATIONS EXTERNES

| Composant externe | Rôle | Livrable attendu |
|-------------------|------|------------------|
| KG-L | Dataset + modèles ML | `KG-L/tools/verses_dataset.py`, `KG-L/ml/verse_classifier.py` |
| VERSES | 522 versets actifs | `VERSES/verses/actifs/` |
| Personae | 7 profils experts | `Personae/personae/*.yaml` |
| VOLTX | Bus unifié 5 canaux | `VOLTX/` (déjà intégré via `voltx_bridge.rs`) |
| WAZAA | Bus événementiel | `WAZAA/` (déjà intégré via `wazaa_bridge.rs`) |

## 3. PLAN D'IMPLÉMENTATION

### Tâche 1 — Orchestrateur ML (N243)
- [x] Workflow `ml_train` créé (`workflows/ml_train/n243-ml-train.yaml`)
- [x] WAZAA bridge créé (`src/bridge/wazaa_bridge.rs`)
- [x] VOLTX bridge créé (`src/bridge/voltx_bridge.rs`) avec 5 canaux
- [x] Agents KG-L créés (`src/agents.rs`)

### Tâche 2 — Validation
- [x] `cargo test` → 38 passed
- [x] `rss_lint.py --depth 4 --check-governance` → PASS
- [x] `pytest agents/ tests/` → 12 passed

## 4. CRITÈRES DE VALIDATION

| Critère | Validation |
|---------|------------|
| Workflows ML créés | Fichiers YAML valides dans `workflows/` |
| Bridges créés | `src/bridge/wazaa_bridge.rs` + `voltx_bridge.rs` compilent |
| Tests passent | `cargo test` + `pytest` PASS |
| Conformité RSS-v2 | `rss_lint.py` PASS |

## 5. ÉTAT OBSERVÉ

**2026-09-15T02:48+02:00** — Proof-of-Life auto-mode SLM :
- [x] PRD-006 créé
- [x] Orchestrateur ML N243 opérationnel
- [x] Compilation vérifiée (`cargo check` → PASS)
- [x] Tests Rust passent (`cargo test --lib` → 38 passed)
- [x] Tests Python passent (`pytest agents/ tests/` → 12 passed)
- [x] Conformité RSS-v2 validée (`rss_lint.py --depth 4 --check-governance` → PASS)

### Preuves d'exécution horodatées

```
[RUST] cargo test --lib -- 2026-09-15T02:48+02:00
  test result: ok. 38 passed; 0 failed; 0 ignored; 0 measured

[PYTHON] pytest agents/test_n243_supervisor.py tests/test_runner_protocol.py -v -- 2026-09-15T02:48+02:00
  ======================= 12 passed in 79.21s =======================

[RSS] rss_lint.py --repo . --depth 4 --check-governance -- 2026-09-15T02:48+02:00
  [PASS] Repo conforme RSS-v2
```

## 6. RÉFÉRENCES

- **PRD-MOC Parent** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-KG-L-ML-TRAINING-PIPELINE-2026-09-15.md`
- **Master** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-KNOWLEDGE-TO-ML-PIPELINE-MASTER-2026-09-15.md`
- **KG-L** : gerivdb/KG-L
- **VERSES** : gerivdb/VERSES
- **Personae** : gerivdb/Personae
- **VOLTX** : gerivdb/VOLTX
- **N243** : gerivdb/N243
