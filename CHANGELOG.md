# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - 2026-09-17

### Added
- Référence à `PRD-MOC-GEN-083` dans `agents/prd_moc_supervisor.md` et `agents/runner-protocol.md`
- Concepts d'ontologie `semantic_combos_catalog` et `ontology_term_gate` dans `ONTOLOGY_DECLARATION.yaml`
- Dépendances `GOVERNANCE-HUB`, `PRD-MOC-GEN-083`, `ontology-term-gate` dans `README.md`
- Point d'entrée binaire N243 : `src/main.rs` (orchestrateur CLI avec clap)
- Module orchestrator : `src/orchestrator.rs`
- Module agent-runner : `src/agent_runner.rs`
- Module wal-emitter : `src/wal_emitter.rs`
- Module bdcp/enforcer : `src/bdcp/enforcer.rs`
- Test d'intégration LLUX 7B `.q243` : `tests/test_llux_q243_integration.rs`

### Governance
- Intégration du catalogue de combos sémantiques invocables (causal dryrun, 14 combination ops, think-do-check, proof-of-life, ontology-term-gate, pre-push-path-audit, branch-lifecycle, domain-links-exporter)
- Validation ontologique avant approval des documents de gouvernance via `ontology_term_gate.py --strict`
- Documentation PRD-011 (orchestrator module & CLI) et PRD-012 (WAZAA integration)

## [1.0.0] - 2026-09-15

### Added
- 4 agents KG-L : `LluxAgent` (Axe 17), `TimxAgent` (Axe 9), `RootxAgent` (Axe 13), `TlmAgent` (Axe 12)
- Workflow `kg_mutation` : orchestration des mutations KG-L
- Workflow `ml_train` : pipeline d'entraînement ML
- WAZAA Bridge : publication/souscription sur le bus événementiel
- VOLTX Bridge : bus unifié 5 canaux (PLIX, PIANO, TALEX, SPIDX, WAZAA)
- Tests d'intégration : `tests/test_n243_integration.rs` (5 tests)
- Documentation opérationnelle : `docs/operationalization.md`

### Changed
- Version Rust : 0.1.0 → 1.0.0
- Architecture : ajout du module `src/bridge/` pour les bridges WAZAA/VOLTX

### Fixed
- `publish` WAZAA bridge : distribution effective aux handlers abonnés
- Ajout de `is_connected()` sur les bridges pour introspection

### Validation
- `cargo test --lib` : 38 passed
- `cargo test --test test_n243_integration` : 5 passed
- `pytest agents/ tests/` : 12 passed
- `rss_lint.py --depth 4 --check-governance` : PASS
