---
type: PRD-MOC
version: "1.0.0"
date: "2026-09-17"
status: accepted
state_observed: "2026-09-15T02:16:00+02:00"
intent_hash: "0xN243_KG_L_ML_ORCHESTRATION_20260915"
author: "N243"
created: "2026-09-15"
id: "PRD-003"
repo: "N243"
title: "N243 KG-L ML Orchestration — Agents & Workflow"
inherits:
  - "PRD-MOC-KG-L-N243-ML-ORCHESTRATION-2026-09-15"
mox_gates:
  - P-108
  - P-109
  - C7
  - C8
source_prd: "GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-KG-L-N243-ML-ORCHESTRATION-2026-09-15.md"
---

# PRD-003 — N243 KG-L ML Orchestration — Agents & Workflow

> **Scope** : N243 repo — intégration du Knowledge Graph (KG-L) avec le méta-orchestrateur
> N243 pour l'orchestration des pipelines ML/IA via 4 agents spécialisés et un workflow
> de mutation KG-L.

## 1. RÉSUMÉ

Implémentation de l'intégration KG-L ↔ N243 pour l'orchestration ML :

| Composant | Description | Fichier |
|-----------|-------------|---------|
| `LluxAgent` | KG-L Axe 17 (Transformer Memory) | `src/agents.rs::LluxAgent` |
| `TimxAgent` | KG-L Axe 9 (Dynamic Systems) | `src/agents.rs::TimxAgent` |
| `RootxAgent` | KG-L Axe 13 (Ontologies) | `src/agents.rs::RootxAgent` |
| `TlmAgent` | KG-L Axe 12 (Ternary Logic) | `src/agents.rs::TlmAgent` |
| `kg_mutation` workflow | Orchestration des mutations KG-L | `workflows/kg_mutation/n243-kg-mutation.yaml` |

## 2. PLAN D'IMPLÉMENTATION

### Tâche 1 — Workflow kg_mutation
- [x] Créer `workflows/kg_mutation/n243-kg-mutation.yaml`
- [x] Définir triggers : `n243.gate.decision`, `wazaa.event`, `manual`
- [x] Définir steps : receive_decision, validate_gf, mutate_kg_l, log_wal, publish_wazaa

### Tâche 2 — Agents KG-L
- [x] `LluxAgent` — transform + index_node
- [x] `TimxAgent` — schedule_train + export_dataset
- [x] `RootxAgent` — analyze_causal + validate_ontology
- [x] `TlmAgent` — evaluate_ternary + detect_oscillation

### Tâche 3 — Validation
- [x] `cargo test` → 0 échec
- [x] `rss_lint.py --depth 4 --check-governance` → PASS
- [x] `pytest agents/ tests/` → 0 échec

## 3. CRITÈRES DE VALIDATION

| Critère | Validation |
|---------|------------|
| Workflow kg_mutation créé | Fichier YAML valide dans `workflows/kg_mutation/` |
| 4 agents Rust implémentés | `LluxAgent`, `TimxAgent`, `RootxAgent`, `TlmAgent` compilent |
| Tests agents | Tests unitaires dans `src/agents.rs` |
| Conformité RSS-v2 | `rss_lint.py` PASS |

## 4. ÉTAT OBSERVÉ

**2026-09-15T02:16+02:00** — Proof-of-Life auto-mode SLM :
- [x] Workflow `kg_mutation` créé
- [x] 4 agents KG-L implémentés dans `src/agents.rs`
- [x] Compilation vérifiée (`cargo check` → PASS)
- [x] Tests Rust passent (`cargo test agents::tests` → 6 passed)
- [x] Tests Python passent (`pytest agents/ tests/` → 12 passed)
- [x] Conformité RSS-v2 validée (`rss_lint.py --depth 4 --check-governance` → PASS)

### Preuves d'exécution horodatées

```
[RUST] cargo test agents::tests -- 2026-09-15T02:15+02:00
  test agents::tests::test_agent_lifecycle ... ok
  test agents::tests::test_agent_registry ... ok
  test agents::tests::test_llux_agent ... ok
  test agents::tests::test_rootx_agent ... ok
  test agents::tests::test_timx_agent ... ok
  test agents::tests::test_tlm_agent ... ok
  test result: ok. 6 passed; 0 failed; 0 ignored; 0 measured

[PYTHON] pytest agents/test_n243_supervisor.py tests/test_runner_protocol.py -v -- 2026-09-15T02:16+02:00
  ======================= 12 passed in 77.08s =======================

[RSS] rss_lint.py --repo . --depth 4 --check-governance -- 2026-09-15T02:16+02:00
  [PASS] Repo conforme RSS-v2
```

## 5. RÉFÉRENCES

- **PRD-MOC Parent** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-KG-L-N243-ML-ORCHESTRATION-2026-09-15.md`
- **KG-L** : gerivdb/KG-L
- **N243** : gerivdb/N243
- **ADR** : ADR-KG-L-N243-ML-ORCHESTRATION-20260915
- **INTENT** : INTENT-KG-L-N243-ML-ORCHESTRATION-20260915
