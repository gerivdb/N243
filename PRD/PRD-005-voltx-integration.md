---
type: PRD-MOC
version: "1.0.0"
date: "2026-09-17"
status: accepted
state_observed: "2026-09-15T02:46:00+02:00"
intent_hash: "0xN243_VOLTX_INTEGRATION_20260915"
author: "N243"
created: "2026-09-15"
id: "PRD-005"
repo: "N243"
title: "N243 VOLTX Integration — Bus Unifié 5 Canaux"
inherits:
  - "PRD-MOC-VOLTX-N243-INTEGRATION-2026-09-15"
mox_gates:
  - P-108
  - P-109
  - C7
  - C8
source_prd: "GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-VOLTX-N243-INTEGRATION-2026-09-15.md"
---

# PRD-005 — N243 VOLTX Integration — Bus Unifié 5 Canaux

> **Scope** : N243 repo — intégration du bus unifié VOLTX avec le méta-orchestrateur N243.
>
> **Source** : `PRD-MOC-VOLTX-N243-INTEGRATION-2026-09-15.md` (proposed, P1)

## 1. RÉSUMÉ

Intégration du bus événementiel VOLTX (5 canaux) avec N243 :

| Canal VOLTX | Runner N243 | Type | Usage ML |
|-------------|-------------|------|----------|
| PLIX → PIANO | LLUX | Vision → Audio | Sonification données |
| PIANO → TALEX | TIMX | Audio → Narration | Feature extraction |
| TALEX → SPIDX | ROOTX | Narration → Graphe | Knowledge extraction |
| SPIDX → WAZAA | TLM-CORE | Graphe → Diffusion | Model serving |
| WAZAA → PLIX | LLUX | Diffusion → Vision | Feedback loop |

## 2. PLAN D'IMPLÉMENTATION

### Tâche 1 — Bridge VOLTX
- [ ] Créer `src/bridge/voltx_bridge.rs`
- [ ] Implémenter `VoltxBridge::register_channel(name, handler)`
- [ ] Implémenter `VoltxBridge::send(channel, payload)`
- [ ] Implémenter 5 canaux : PLIX, PIANO, TALEX, SPIDX, WAZAA

### Tâche 2 — Tests
- [ ] `cargo test` → 0 échec
- [ ] `rss_lint.py --depth 4 --check-governance` → PASS

## 3. CRITÈRES DE VALIDATION

| Critère | Validation |
|---------|------------|
| VOLTX bridge compilé | `cargo check` PASS |
| 5 canaux enregistrés | Tests unitaires PASS |
| Conformité RSS-v2 | `rss_lint.py` PASS |

## 4. ÉTAT OBSERVÉ

**2026-09-15T02:46+02:00** — Proof-of-Life auto-mode SLM :
- [x] PRD-005 créé
- [x] VOLTX bridge implémenté (`src/bridge/voltx_bridge.rs`)
- [x] 5 canaux VOLTX enregistrés : PLIX, PIANO, TALEX, SPIDX, WAZAA
- [x] Compilation vérifiée (`cargo check` → PASS)
- [x] Tests Rust passent (`cargo test --lib` → 38 passed)
- [x] Tests Python passent (`pytest agents/ tests/` → 12 passed)
- [x] Conformité RSS-v2 validée (`rss_lint.py --depth 4 --check-governance` → PASS)

### Preuves d'exécution horodatées

```
[RUST] cargo test --lib -- 2026-09-15T02:46+02:00
  test result: ok. 38 passed; 0 failed; 0 ignored; 0 measured

[PYTHON] pytest agents/test_n243_supervisor.py tests/test_runner_protocol.py -v -- 2026-09-15T02:47+02:00
  ======================= 12 passed in 79.21s =======================

[RSS] rss_lint.py --repo . --depth 4 --check-governance -- 2026-09-15T02:48+02:00
  [PASS] Repo conforme RSS-v2
```

## 5. RÉFÉRENCES

- **PRD-MOC Parent** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-VOLTX-N243-INTEGRATION-2026-09-15.md`
- **VOLTX** : gerivdb/VOLTX
- **N243** : gerivdb/N243
- **WAZAA** : gerivdb/WAZAA
