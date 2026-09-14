---
type: PRD-MOC
version: "1.0.0"
date: "2026-09-14"
status: proposed
state_observed: "2026-09-14T22:07:00+02:00"
intent_hash: "0xN243_GATE_ORCHESTRATION_RUNNER_PROTOCOL_20260914"
author: "N243"
created: "2026-09-14"
id: "PRD-001"
repo: "N243"
title: "N243 Gate Orchestration & Runner Protocol Integration"
inherits:
  - "moc-governance"
  - "PRD-MOC-ECOSYSTEM-MEMORY-ARCHITECTURE-2026-08-28"
mox_gates:
  - P-108
  - P-109
  - C7
  - C8
source_intent: "GOVERNANCE-HUB/INTENTS/INTENT-2026-08-22-KG-L-WAZAA-N243-SOUVERAIN-V0_5.md"
source_adr: "GOVERNANCE-HUB/ADR/ADR-2026-08-28-003-N243-MEMORY-GATE.md"
source_prd: "REPO-STANDARDS/PRD/PRD-001-rss-v2-artifact-policy.md"
---

# PRD MOC – N243 Gate Orchestration & Runner Protocol Integration

> **Scope** : N243 repo — orchestration des gates ternaires L5/L6, intégration du runner protocol,
> et supervision PRD/MOC autonome.
> **Statut** : proposed — en attente de validation HITL et review cross-repo.

## 1. RÉSUMÉ EXÉCUTIF

> **Objet** : formaliser l'évolution de N243 vers un méta-orchestrateur ternaire complet,
> intégrant le **runner protocol** (L6), le **memory gate** (L5), et le **superviseur PRD/MOC**
> comme capacités de première classe.
>
> **Contexte** : les commits récents de N243 ont ajouté :
> - `src/gates/runner_protocol.rs` — protocole d'orchestration des runners L*
> - `src/gates/memory_gate.rs` — gate mémoire pour écritures
> - `agents/prd_moc_supervisor.py` — agent superviseur PRD/MOC
> - WAL ternaire avec fixtures de test
>
> Ce PRD-MOC structure ces travaux dispersés en une roadmap cohérente et conforme RSS-v2.3.

## 2. CONTEXTE ET PÉRIMÈTRE

### 2.1 Contexte

N243 est le **méta-orchestrateur ternaire** de l'écosystème gerivdb. Ses responsabilités :

| Domaine | Capacité actuelle | Manque identifié |
|---------|-------------------|------------------|
| Gates ternaires | L5 (domain), L6 (runner) | Pas de protocole unifié d'orchestration |
| WAL ternaire | Journal append-only | Pas de reprise sur échec (replay) |
| Supervisor | Agent PRD/MOC basique | Pas de boucle de validation autonome |
| WAZAA bridge | Topics `n243.gates` | Pas de federation ni de monitoring |

### 2.2 Périmètre

| Strate | Composants | Impact |
|--------|-----------|--------|
| L4-TOOLS | N243 (ce repo) | Core : gates, WAL, supervisor, runner protocol |
| L1-INFRA | WAZAA | Bus temps-réel pour messages `gate.decision` |
| L2-PLATFORM | KG-L | Indexation causale des décisions N243 |
| L2-PLATFORM | CTULU | Vue spectrale du graphe N243 |
| L0-CANON | GOVERNANCE-HUB | ADR, INTENT, PRD-MOC source de vérité |

### 2.3 Principes directeurs

1. **Ternarité native** : toute décision est APPROUVER/SUSPENDRE/REJETER — pas de booléen
2. **Local-first** : le repo N243 est la source de vérité de son orchestration
3. **WAL comme mémoire** : toute décision est tracée, rejouable, auditable
4. **Supervision autonome** : le superviseur PRD/MOC valide ses propres propositions
5. **Conformité RSS-v2.3** : artefacts structurés, frontmatter valide, index maintenu

## 3. ARCHITECTURE CIBLE

### 3.1 Composants N243

```
N243/
├── src/
│   ├── gates/
│   │   ├── mod.rs              ← Module public
│   │   ├── l5.rs               ← Gate domaine (APPROUVER/SUSPENDRE/REJETER)
│   │   ├── l6.rs               ← Gate runner (orchestration L*)
│   │   ├── memory_gate.rs      ← Gate mémoire (écritures)
│   │   ├── runner_protocol.rs  ← Protocole runners L* (NOUVEAU)
│   │   └── types.rs            ← Types partagés
│   └── ...
├── agents/
│   ├── prd_moc_supervisor.py   ← Superviseur PRD/MOC (NOUVEAU)
│   └── test_n243_supervisor.py ← Tests supervisor (NOUVEAU)
├── wal/
│   ├── ternary-wal.jsonl       ← WAL principal
│   ├── test-n243-*.jsonl       ← Fixtures de test
│   └── test/                   ← Répertoire de tests WAL
├── PRD/
│   └── PRD-001-*.md       ← Ce document
├── ADR/
│   └── ADR-2026-08-28-003-N243-MEMORY-GATE.md
└── ...
```

### 3.2 Flux d'orchestration

```
Writer ──▶ [N243 Gate] ──▶ WAZAA topic "n243.gates"
                              │
                              ▼
                         [Runner Protocol]
                         L* runners (LLUX, RLM-243, ...)
                              │
                              ▼
                         [WAL Ternaire]
                         Convergence / Divergence / Oscillation
                              │
                              ▼
                         [KG-L Indexer]
                         Causal edges + CTULU spectral view
```

### 3.3 Runner Protocol (L6)

Le `runner_protocol.rs` définit l'interface d'orchestration des runners L* :

```rust
pub enum RunnerCommand {
    Run { input: Input, target: RunnerTarget },
    Stop { id: String },
    Snapshot { id: String },
    Restore { id: String, snapshot: SnapshotRef },
}

pub enum RunnerTarget {
    LLUX,
    RLM243,
    TIMX,
    ROOTX,
    TLMCORE,
}

pub struct RunnerResult {
    pub decision: TernaryDecision,
    pub output: Output,
    pub wal_entry: WalEntryRef,
}
```

### 3.4 Supervisor PRD/MOC

L'agent `prd_moc_supervisor.py` valide les documents de gouvernance :

```python
class PRDMOCSupervisor:
    def validate(self, doc_path: str) -> GateDecision:
        """Valide un PRD/MOC selon les règles de gouvernance."""

    def route(self, doc: GovernanceDocument) -> RoutingDecision:
        """Route le document vers le bon dépôt/acteur."""

    def propose_adr(self, gap: GovernanceGap) -> ADRProposal:
        """Propose un ADR pour combler un gap identifié."""
```

## 4. PLAN D'IMPLÉMENTATION

### Sprint 1 — WAL Ternaire + Replay (S1.1 — S1.3)

| Tâche | Action | Validation |
|-------|--------|-----------|
| S1.1 | Implémenter `WAL::replay()` pour reprise sur échec | Test : crash simulé → replay cohérent |
| S1.2 | Ajouter `WAL::compact()` pourTTL 30j | Test : entrées anciennes supprimées |
| S1.3 | Fixtures WAL pour tests (APPROUVER/SUSPENDRE/REJETER) | `cargo test` passe |

### Sprint 2 — Runner Protocol Stabilisation (S2.1 — S2.3)

| Tâche | Action | Validation |
|-------|--------|-----------|
| S2.1 | Finaliser `RunnerCommand` + `RunnerResult` | Compilation Zig 0.15 OK |
| S2.2 | Intégrer runner_protocol avec WAZAA topics | `wazaa send` → runner exécute → WAL |
| S2.3 | Tests d'intégration runner protocol | `pytest tests/` passe |

### Sprint 3 — Supervisor PRD/MOC (S3.1 — S3.3)

| Tâche | Action | Validation |
|-------|--------|-----------|
| S3.1 | Étendre `prd_moc_supervisor.py` — validation frontmatter | Hook pre-commit accepte |
| S3.2 | Connecter supervisor → WAZAA topic `prd_moc.gate` | Décisions reçues par WAZAA |
| S3.3 | Tests unitaires supervisor | `pytest agents/` passe |

### Sprint 4 — Conformité RSS-v2.3 (S4.1 — S4.3)

| Tâche | Action | Validation |
|-------|--------|-----------|
| S4.1 | Créer `ONTOLOGY_DECLARATION.yaml` | ✅ Fait |
| S4.2 | Créer `PRD/PRD-000-index.md` | Index auto-généré |
| S4.3 | Vérifier `rss_lint.py` sur N243 | Exit 0, 0 erreur |

## 5. CRITÈRES DE VALIDATION

| Critère | Validation |
|---------|------------|
| WAL replay fonctionnel | Crash simulé + replay → état cohérent |
| Runner protocol end-to-end | `wazaa send` → runner exécute → WAL mis à jour |
| Supervisor PRD/MOC autonome | Valide un PRD/MOC sans HITL |
| Conformité RSS-v2.3 | `rss_lint.py --repo D:\DO\WEB\TOOLS\L4-TOOLS\N243` → exit 0 |
| Tests passent | `cargo test` + `pytest agents/` + `pytest tests/` → 0 échec |
| Ontologie déclarée | `ONTOLOGY_DECLARATION.yaml` présent et valide |

## 6. RISQUES ET MITIGATIONS

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| WAL replay lent sur gros fichiers | Moyenne | Élevé | Chunking + streaming |
| Runner protocol coupling fort avec WAZAA | Faible | Moyen | Interface abstraite + mock tests |
| Supervisor boucle infinie | Moyenne | Élevé | Timeout + circuit breaker |
| Dérive ontologique N243 ↔ NEXUS | Faible | Moyen | ARGUS surveillance + `ONTOLOGY_DECLARATION.yaml` |

## 7. RÉFÉRENCES

- ADR : `ADR-2026-08-28-003-N243-MEMORY-GATE`
- PRD-MOC : `PRD-MOC-ECOSYSTEM-MEMORY-ARCHITECTURE-2026-08-28`
- PRD-MOC : `PRD-MOC-KG-L-WAZAA-N243-SOUVERAIN-2026-08-22`
- Standard : `REPO-STANDARDS/docs/RSS-v2.md`
- Schéma PRD : `REPO-STANDARDS/config/schemas/prd.schema.yaml`
- WAZAA protocol : `WAZAA/docs/protocols/swarm-messages.yaml`

## 8. ÉTAT OBSERVÉ

**2026-09-15T00:30+02:00** — Proof-of-Life auto-mode SLM :
- [x] Branche feature créée
- [x] `ONTOLOGY_DECLARATION.yaml` créé
- [x] `PRD/` directory créé
- [x] `PRD/PRD-N243-001-gate-orchestration-runner-protocol.md` créé (ce document)
- [x] `PRD/PRD-000-index.md` créé
- [x] WAL replay implémenté (Rust + tests) — `src/wal.rs::replay()`
- [x] WAL compact TTL 30j implémenté (Rust + tests) — `src/wal.rs::compact_ttl()`
- [x] Runner protocol finalisé (Rust) — `src/gates/runner_protocol.rs`
- [x] Supervisor frontmatter validator étendu (S3.1) — `agents/prd_moc_supervisor.py::validate_frontmatter()`
- [x] Supervisor connecté à WAZAA topic `prd_moc.gate` (S3.2) — `agents/prd_moc_supervisor.py::_publish_wazaa()`
- [x] Tests unitaires supervisor (S3.3) — `agents/test_n243_supervisor.py`
- [x] Conformité RSS-v2.3 validée (`rss_lint.py --depth 4` → PASS)

### Preuves d'exécution horodatées

```
[WAL] cargo test wal::tests -- 2026-09-15T00:28+02:00
  test wal::tests::test_n243_wal_record ... ok
  test wal::tests::test_n243_wal_oscillation_detection ... ok
  test wal::tests::test_n243_wal_compact ... ok
  test wal::tests::test_n243_wal_replay ... ok
  test wal::tests::test_n243_wal_compact_ttl ... ok
  test result: ok. 5 passed; 0 failed

[SUPERVISOR] pytest agents/test_n243_supervisor.py -v -- 2026-09-15T00:29+02:00
  agents/test_n243_supervisor.py::test_ternary_wal PASSED
  agents/test_n243_supervisor.py::test_n243_supervisor_approve PASSED
  agents/test_n243_supervisor.py::test_n243_supervisor_suspend PASSED
  agents/test_n243_supervisor.py::test_n243_supervisor_reject PASSED
  agents/test_n243_supervisor.py::test_n243_narrative PASSED
  ======================= 5 passed in 32.63s =======================

[RSS] rss_lint.py --repo . --depth 4 -- 2026-09-15T00:30+02:00
  [PASS] Repo conforme RSS-v2
```
