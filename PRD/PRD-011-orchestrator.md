---
type: PRD-MOC
version: "1.0.0"
date: "2026-09-17"
status: proposed
state_observed: "2026-09-17T03:16:00+02:00"
intent_hash: "0xN243_ORCHESTRATOR_20260917"
author: "N243"
created: "2026-09-17"
id: "PRD-011"
repo: "N243"
title: "N243 Orchestrator — Module & CLI"
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

# PRD-011 — N243 Orchestrator — Module & CLI

> **Scope** : N243 repo — module `orchestrator`, CLI binaire `main.rs`, et intégration
> des modules core (`agent-runner`, `wal-emitter`, `bdcp/enforcer`).
> **Statut** : proposed — en attente de validation HITL et review cross-repo.

## 1. RÉSUMÉ EXÉCUTIF

Ce PRD-MOC documente l'implémentation du module orchestrateur de N243 et de son point d'entrée binaire, conformément à la tâche #1 du MASTER.

### Livrables

| Livrable | Fichier | Statut |
|---|---|---|
| Module orchestrator | `src/orchestrator.rs` | ✅ Implémenté |
| CLI binaire | `src/main.rs` | ✅ Implémenté |
| Intégration agent-runner | `src/agent_runner.rs` | ✅ Implémenté |
| Intégration wal-emitter | `src/wal_emitter.rs` | ✅ Implémenté |
| Intégration bdcp/enforcer | `src/bdcp/enforcer.rs` | ✅ Implémenté |

## 2. ARCHITECTURE

```
N243/
├── src/
│   ├── main.rs                 ← CLI binaire (clap)
│   ├── orchestrator.rs         ← Module orchestrator core
│   ├── agent_runner.rs         ← Protocole runners L*
│   ├── wal_emitter.rs          ← Émission WAL append-only
│   ├── bdcp/
│   │   ├── mod.rs              ← Module BDCP
│   │   └── enforcer.rs         ← Point d'entrée BDCP
│   ├── agents.rs               ← Agents core
│   ├── workflows.rs            ← Workflows
│   ├── wal.rs                  ← WAL
│   ├── bdcp.rs                 ← (legacy, redirige vers bdcp/mod.rs)
│   └── ...
```

## 3. COMPOSANTS

### 3.1 Orchestrator

Le module `orchestrator.rs` fournit :

- `OrchestratorState` : énumération d'état (`Idle`, `Running`, `Failed`)
- `Orchestrator` : structure principale
  - `registry: AgentRegistry`
  - `wal: N243WAL`
  - `bdcp: N243BDCPGovernor`
  - `wazaa: WazaaBridge`
  - `voltx: VoltxBridge`
  - `workflow_registry: N243WorkflowRegistry`
  - `validator: WorkflowValidator`

### 3.2 CLI Binaire

Le CLI expose les commandes suivantes :

| Commande | Description |
|---|---|
| `status` | Affiche l'état du système N243 |
| `validate-workflows` | Valide les workflows enregistrés |
| `list-agents` | Liste les agents enregistrés |
| `trigger-workflow <id>` | Déclenche un workflow |
| `wal-tail <limit>` | Affiche les entrées WAL récentes |
| `bdcp-status` | Vérifie le statut BDCP |

## 4. CRITÈRES DE VALIDATION

| Critère | Validation |
|---------|------------|
| Module orchestrator compile | `cargo check` PASS |
| CLI binaire compile | `cargo check` PASS |
| Tests passent | `cargo test` → 47 passed |
| Intégration LLUX validée | `tests/test_llux_q243_integration.rs` → 3 passed |

## 5. ÉTAT OBSERVÉ

**2026-09-17T03:16+02:00** — Proof-of-Life auto-mode SLM :
- [x] Module `orchestrator.rs` créé
- [x] CLI binaire `main.rs` créé
- [x] Module `agent_runner.rs` créé
- [x] Module `wal_emitter.rs` créé
- [x] Module `bdcp/enforcer.rs` créé
- [x] `cargo test` → 47 passed
- [x] Intégration LLUX 7B `.q243` validée

### Preuves d'exécution horodatées

```
[RUST] cargo test -- 2026-09-17T03:13+02:00
  test result: ok. 47 passed; 0 failed; 0 ignored; 0 measured

[RUST] cargo test --test test_llux_q243_integration -- 2026-09-17T03:13+02:00
  running 3 tests
  test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured

[GIT] git push origin main -- 2026-09-17T03:13+02:00
  To https://github.com/gerivdb/N243.git
  c7702e0..9729a36  main -> main
```

## 6. RÉFÉRENCES

- **MASTER** : `PRD-MOC-N243-MASTER.md`
- **ADR** : ADR-2026-06-28-001-LOGICAL-ARCHITECTURE-N1-N4
- **IntentHash** : 0xN243_META_ORCHESTRATOR_20260801
