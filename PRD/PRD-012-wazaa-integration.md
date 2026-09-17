---
type: PRD-MOC
version: "1.0.0"
date: "2026-09-17"
status: accepted
state_observed: "2026-09-17T03:18:00+02:00"
intent_hash: "0xN243_WAZAA_INTEGRATION_20260917"
author: "N243"
created: "2026-09-17"
id: "PRD-012"
repo: "N243"
title: "N243 WAZAA Integration — Bridge & Topics"
inherits:
  - "PRD-MOC-N243-MASTER-2026-09-16"
  - "PRD-001-gate-orchestration-runner-protocol"
mox_gates:
  - P-108
  - P-109
  - C7
  - C8
source_prd: "PRD-MOC-N243-MASTER.md"
---

# PRD-012 — N243 WAZAA Integration — Bridge & Topics

> **Scope** : N243 repo — intégration du bus événementiel WAZAA avec le méta-orchestrateur N243.
> **Statut** : proposed — en attente de validation HITL et review cross-repo.

## 1. RÉSUMÉ EXÉCUTIF

Ce PRD-MOC documente l'intégration WAZAA dans N243, couvrant le bridge Rust,
les topics officiels, et la supervision des événements du bus.

### Livrables

| Livrable | Fichier | Statut |
|---|---|---|
| WAZAA bridge | `src/bridge/wazaa_bridge.rs` | ✅ Implémenté |
| Topics WAZAA | `src/bridge/wazaa_bridge.rs` + docs | ✅ Implémenté |
| Tests bridge | `tests/test_wazaa_bridge_integration.rs` | ✅ Implémenté |

## 2. ARCHITECTURE

```
N243/
├── src/
│   ├── bridge/
│   │   ├── mod.rs              ← Module bridge
│   │   ├── wazaa_bridge.rs     ← Bridge WAZAA
│   │   └── voltx_bridge.rs     ← Bridge VOLTX
│   ├── orchestrator.rs         ← Orchestrator core
│   └── ...
├── tests/
│   └── test_wazaa_bridge_integration.rs
└── PRD/
    └── PRD-012-wazaa-integration.md  ← Ce document
```

## 3. COMPOSANTS

### 3.1 WAZAA Bridge

Le module `src/bridge/wazaa_bridge.rs` fournit :

- `WazaaBridge` : bridge principal
  - `connect()` / `disconnect()`
  - `publish(topic, payload)`
  - `subscribe(topic, handler)`
  - `is_connected()`

- `WazaaMessage` : message transporté sur le bus
  - `topic`, `payload`, `timestamp`, `source`

### 3.2 Topics WAZAA

| Topic | Usage | Émetteur | Récepteur |
|---|---|---|---|
| `n243.gates` | Décisions de gates L5/L6 | N243 | WAZAA |
| `n243.runners` | Événements runners L* | N243 | WAZAA |
| `n243.wal` | Événements WAL ternaire | N243 | WAZAA |
| `prd_moc.gate` | Validation PRD/MOC | Supervisor | WAZAA |
| `swarm.hello` / `swarm.bye` | Présence essaim | Kilo/ACT | WAZAA |

## 4. FLUX D'INTÉGRATION

```
N243 Gate ──▶ publish("n243.gates", decision) ──▶ WAZAA bus
                                                        │
Runner Protocol ──▶ publish("n243.runners", event) ──▶ WAZAA bus
                                                        │
WAL Emitter ──▶ publish("n243.wal", entry) ──▶ WAZAA bus
```

## 5. CRITÈRES DE VALIDATION

| Critère | Validation |
|---------|------------|
| Bridge compile | `cargo check` PASS |
| Bridge connect/disconnect | Tests unitaires PASS |
| Publish/subscribe | Tests d'intégration PASS |
| Topics documentés | Ce document + code |
| Tests passent | `cargo test` → 47 passed |

## 6. ÉTAT OBSERVÉ

**2026-09-17T03:18+02:00** — Proof-of-Life auto-mode SLM :
- [x] WAZAA bridge implémenté (`src/bridge/wazaa_bridge.rs`)
- [x] 5 topics WAZAA documentés
- [x] Tests d'intégration WAZAA passent (`tests/test_wazaa_bridge_integration.rs` → 5 passed)
- [x] `cargo test` → 47 passed

### Preuves d'exécution horodatées

```
[RUST] cargo test --test test_wazaa_bridge_integration -- 2026-09-17T03:13+02:00
  running 5 tests
  test result: ok. 5 passed; 0 failed; 0 ignored; 0 measured

[RUST] cargo test -- 2026-09-17T03:13+02:00
  test result: ok. 47 passed; 0 failed; 0 ignored; 0 measured

[GIT] git push origin main -- 2026-09-17T03:13+02:00
  To https://github.com/gerivdb/N243.git
  c7702e0..9729a36  main -> main
```

## 7. RÉFÉRENCES

- **MASTER** : `PRD-MOC-N243-MASTER.md`
- **PRD-011** : `PRD/PRD-011-orchestrator.md`
- **ADR** : ADR-2026-06-28-001-LOGICAL-ARCHITECTURE-N1-N4
- **IntentHash** : 0xN243_META_ORCHESTRATOR_20260801
