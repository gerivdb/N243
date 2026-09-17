# N243 — Meta-Orchestrateur Cognitif L*

**Version** : 1.0.0
**Statut** : RELEASED
**Strate** : L4-TOOLS
**IntentHash** : 0xN243_META_ORCHESTRATOR_20260801

---

## Vision

N243 orchestre les 5 runners cognitifs core de l'écosystème L* :
- **LLUX** (BitNet 1.58b)
- **RLM-243** (Release Lifecycle)
- **TIMX** (Temporel / Features)
- **ROOTX** (Racines Symboliques)
- **TLM-CORE** (Logique Ternaire)

S'appuie sur **WAZAA** (`gerivdb/WAZAA`, L4) comme infrastructure d'orchestration : bus événementiel Intent, WAL append-only, EventServer WebSocket (pivot 2026-08-23, Buzz@block abandonné dans ENV2).

---

## Structure

N243/
├── Cargo.toml
├── README.md
├── CHANGELOG.md
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
│   ├── bridge/
│   │   ├── mod.rs              ← Module bridge
│   │   ├── wazaa_bridge.rs     ← Bridge WAZAA
│   │   └── voltx_bridge.rs     ← Bridge VOLTX (5 canaux)
│   └── ...
├── workflows/
│   ├── kg_mutation/
│   │   └── n243-kg-mutation.yaml
│   ├── ml_train/
│   │   └── n243-ml-train.yaml
│   ├── personae_ingest/
│   │   └── n243-personae-ingest.yaml
│   └── verses_ingest/
│       └── n243-verses-ingest.yaml
├── tests/
│   ├── test_llux_q243_integration.rs
│   ├── test_personae_ingest_workflow.rs
│   ├── test_verses_ingest_workflow.rs
│   ├── test_kg_mutation_workflow.rs
│   ├── test_ml_train_workflow.rs
│   ├── test_voltx_bridge_integration.rs
│   └── test_cross_bridge_integration.rs
└── PRD/
    ├── PRD-001-gate-orchestration-runner-protocol.md
    ├── PRD-002-automation-primitives.md
    ├── PRD-003-kg-l-ml-orchestration.md
    ├── PRD-004-operationalization.md
    ├── PRD-005-voltx-integration.md
    ├── PRD-006-ml-training-pipeline.md
    ├── PRD-007-integration-tests.md
    ├── PRD-008-release-v1.md
    ├── PRD-009-personae-kg-l-integration.md
    ├── PRD-010-verses-kg-l-integration.md
    ├── PRD-011-orchestrator.md
    └── PRD-012-wazaa-integration.md

## Dépendances

| Dépendance | Chemin | Rôle |
|------------|--------|------|
| WAZAA | ../WAZAA/ | Bus Intent, WAL emitter, EventServer, workflow |
| LLUX | PATH | Runner LLM |
| RLM-243 | PATH | Runner Release |
| TIMX | PATH | Runner Temporel |
| ROOTX | PATH | Runner Symbolique |
| TLM-CORE | PATH | Runner Ternaire |
| GOVERNANCE-HUB | ../GOVERNANCE-HUB/ | PRD-MOC, ADR, ontology validation |
| PRD-MOC-GEN-083 | ../GOVERNANCE-HUB/PRD-MOC/general/ | Semantic combos catalog |
| ontology-term-gate | ../GOVERNANCE-HUB/scripts/ | Ontology validation before approval |

## Quick Start

cd D:/DO/WEB/TOOLS/L4-TOOLS/N243
cargo build
cargo run

## CLI

```bash
n243 status
n243 validate-workflows
n243 list-agents
n243 trigger-workflow <id>
n243 wal-tail <limit>
n243 bdcp-status
```

## Tests

```bash
cargo test
cargo test --test test_llux_q243_integration
cargo test --test test_personae_ingest_workflow
cargo test --test test_verses_ingest_workflow
cargo test --test test_kg_mutation_workflow
cargo test --test test_ml_train_workflow
cargo test --test test_voltx_bridge_integration
cargo test --test test_cross_bridge_integration
```
