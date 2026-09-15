---
type: PRD-MOC
version: "1.0.0"
date: "2026-09-15"
status: proposed
state_observed: "2026-09-15T03:35:00+02:00"
intent_hash: "0xN243_VERSES_KG_L_INTEGRATION_20260915"
author: "N243"
created: "2026-09-15"
id: "PRD-010"
repo: "N243"
title: "N243 VERSES-KG-L Integration — Orchestration"
inherits:
  - "PRD-MOC-VERSES-KG-L-INTEGRATION-2026-09-15"
mox_gates:
  - P-108
  - P-109
  - C7
  - C8
source_prd: "GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-VERSES-KG-L-INTEGRATION-2026-09-15.md"
---

# PRD-010 — N243 VERSES-KG-L Integration — Orchestration

> **Scope** : N243 repo — orchestration de l'intégration VERSES ↔ KG-L.
> Les mappings et les nœuds KG-L restent dans KG-L et VERSES.
> N243 fournit l'orchestrateur, le WAL, la supervision ternaire et l'intégration VOLTX/WAZAA.
>
> **Source** : `PRD-MOC-VERSES-KG-L-INTEGRATION-2026-09-15.md` (proposed, P1)

## 1. RÉSUMÉ

Orchestration N243 de l'intégration VERSES ↔ KG-L :

| Composant N243 | Description | Fichier |
|----------------|-------------|---------|
| `verses_ingest` workflow | Pipeline ingestion VERSES → KG-L | `workflows/verses_ingest/n243-verses-ingest.yaml` |
| Agents KG-L | LluxAgent, TimxAgent, RootxAgent, TlmAgent | `src/agents.rs` |
| WAZAA Bridge | Publication événements `verse.updated` | `src/bridge/wazaa_bridge.rs` |
| VOLTX Bridge | 5 canaux intégrés | `src/bridge/voltx_bridge.rs` |

## 2. INTÉGRATIONS EXTERNES

| Composant externe | Rôle | Livrable attendu |
|-------------------|------|------------------|
| VERSES | 522 versets actifs | `VERSES/verses/actifs/` |
| KG-L | Knowledge Graph 35 axes | `KG-L/integrations/verses_bridge.py` |
| VOLTX | Bus unifié 5 canaux | `VOLTX/` (déjà intégré) |
| WAZAA | Bus événementiel | `WAZAA/` (déjà intégré) |

## 3. PLAN D'IMPLÉMENTATION

### Tâche 1 — Orchestrateur VERSES-KG-L (N243)
- [x] Bridges WAZAA/VOLTX opérationnels
- [x] Agents KG-L créés
- [ ] Workflow `verses_ingest` à créer
- [ ] Publier événements `verse.updated` via WAZAA/VOLTX

### Tâche 2 — Validation
- [ ] `cargo test` → 0 échec
- [ ] `rss_lint.py --depth 4 --check-governance` → PASS

## 4. ÉTAT OBSERVÉ

**2026-09-15T03:38+02:00** — Proof-of-Life auto-mode SLM :
- [x] PRD-010 créé
- [x] Workflow `verses_ingest` créé (`workflows/verses_ingest/n243-verses-ingest.yaml`)
- [x] Compilation vérifiée (`cargo check` → PASS)
- [x] Tests Rust passent (`cargo test --lib` → 38 passed)
- [x] Conformité RSS-v2 validée (`rss_lint.py --depth 4 --check-governance` → PASS)

### Preuves d'exécution horodatées

```
[RUST] cargo test --lib -- 2026-09-15T03:38+02:00
  test result: ok. 38 passed; 0 failed; 0 ignored; 0 measured

[RSS] rss_lint.py --repo . --depth 4 --check-governance -- 2026-09-15T03:39+02:00
  [PASS] Repo conforme RSS-v2
```

## 5. RÉFÉRENCES

- **PRD-MOC Parent** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-VERSES-KG-L-INTEGRATION-2026-09-15.md`
- **Master** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-KNOWLEDGE-TO-ML-PIPELINE-MASTER-2026-09-15.md`
- **VERSES** : gerivdb/VERSES
- **KG-L** : gerivdb/KG-L
- **N243** : gerivdb/N243
