---
type: PRD-MOC
version: "1.0.0"
date: "2026-09-17"
status: accepted
state_observed: "2026-09-15T03:10:00+02:00"
intent_hash: "0xN243_PERSONAE_KG_L_INTEGRATION_20260915"
author: "N243"
created: "2026-09-15"
id: "PRD-009"
repo: "N243"
title: "N243 Personae-KG-L Integration — Orchestration"
inherits:
  - "PRD-MOC-PERSONAE-KG-L-INTEGRATION-2026-09-15"
mox_gates:
  - P-108
  - P-109
  - C7
  - C8
source_prd: "GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-PERSONAE-KG-L-INTEGRATION-2026-09-15.md"
---

# PRD-009 — N243 Personae-KG-L Integration — Orchestration

> **Scope** : N243 repo — orchestration de l'intégration Personae ↔ KG-L.
> Les mappings YAML → RDF et les nœuds KG-L restent dans KG-L.
> N243 fournit l'orchestrateur, le WAL, la supervision ternaire et l'intégration VOLTX/WAZAA.
>
> **Source** : `PRD-MOC-PERSONAE-KG-L-INTEGRATION-2026-09-15.md` (proposed, P1)

## 1. RÉSUMÉ

Orchestration N243 de l'intégration Personae ↔ KG-L :

| Personae | Section | Rôle KG-L | Axe KG-L |
|----------|---------|-----------|----------|
| poincare | archi, perf | Structure | Axe 3 (Topologie) |
| musk | code, sdk | Innovation | Axe 18 (Darwinien) |
| lecun | ml, code | Deep Learning | Axe 16 (GNN) |
| karpathy | code, ml | Efficiency | Axe 7 (Complexité) |
| bellard | perf, code | Optimization | Axe 21 (Thermo) |
| steinberger | perf, ml | Performance | Axe 4 (Hilbert) |
| maxwell | perf, physics | Budget | Axe 21 (Thermo) |

## 2. INTÉGRATIONS EXTERNES

| Composant externe | Rôle | Livrable attendu |
|-------------------|------|------------------|
| Personae | 7 profils experts | `Personae/personae/*.yaml` |
| KG-L | Knowledge Graph | `KG-L/integrations/personae_mapper.py` |
| VOLTX | Bus unifié 5 canaux | `VOLTX/` (déjà intégré via `voltx_bridge.rs`) |
| WAZAA | Bus événementiel | `WAZAA/` (déjà intégré via `wazaa_bridge.rs`) |

## 3. PLAN D'IMPLÉMENTATION

### Tâche 1 — Orchestrateur Personae-KG-L (N243)
- [x] Bridges WAZAA/VOLTX opérationnels
- [x] Agents KG-L créés (LluxAgent, TimxAgent, RootxAgent, TlmAgent)
- [x] Workflow `personae_ingest` créé (`workflows/personae_ingest/n243-personae-ingest.yaml`)
- [x] Publier événements `personae.updated` via WAZAA/VOLTX

### Tâche 2 — Validation
- [x] `cargo test` → 0 échec
- [x] `rss_lint.py --depth 4 --check-governance` → PASS

## 4. CRITÈRES DE VALIDATION

| Critère | Validation |
|---------|------------|
| Workflow personae_ingest créé | Fichier YAML valide dans `workflows/` |
| Bridges opérationnels | `src/bridge/wazaa_bridge.rs` + `voltx_bridge.rs` compilent |
| Tests passent | `cargo test` PASS |
| Conformité RSS-v2 | `rss_lint.py` PASS |

## 5. ÉTAT OBSERVÉ

**2026-09-15T03:16+02:00** — Proof-of-Life auto-mode SLM :
- [x] PRD-009 créé
- [x] Workflow `personae_ingest` créé (`workflows/personae_ingest/n243-personae-ingest.yaml`)
- [x] Compilation vérifiée (`cargo check` → PASS)
- [x] Tests Rust passent (`cargo test --lib` → 38 passed)
- [x] Tests Python passent (`pytest agents/ tests/` → 12 passed)
- [x] Conformité RSS-v2 validée (`rss_lint.py --depth 4 --check-governance` → PASS)

**2026-09-17T03:24+02:00** — Proof-of-Life update: test d'intégration workflow :
- [x] `tests/test_personae_ingest_workflow.rs` → 3 passed
- [x] `cargo test` → 47 passed

### Preuves d'exécution horodatées

```
[RUST] cargo test --lib -- 2026-09-15T03:16+02:00
  test result: ok. 38 passed; 0 failed; 0 ignored; 0 measured

[PYTHON] pytest agents/test_n243_supervisor.py tests/test_runner_protocol.py -v -- 2026-09-15T03:17+02:00
  ======================= 12 passed in 69.21s =======================

[RSS] rss_lint.py --repo . --depth 4 --check-governance -- 2026-09-15T03:18+02:00
  [PASS] Repo conforme RSS-v2

[RUST] cargo test --test test_personae_ingest_workflow -- 2026-09-17T03:24+02:00
  running 3 tests
  test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured

[GIT] git push origin main -- 2026-09-17T03:24+02:00
  To https://github.com/gerivdb/N243.git
  30355d0..0476725  main -> main
```

## 6. RÉFÉRENCES

- **PRD-MOC Parent** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-PERSONAE-KG-L-INTEGRATION-2026-09-15.md`
- **Master** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-KNOWLEDGE-TO-ML-PIPELINE-MASTER-2026-09-15.md`
- **Personae** : gerivdb/Personae
- **KG-L** : gerivdb/KG-L
- **N243** : gerivdb/N243
