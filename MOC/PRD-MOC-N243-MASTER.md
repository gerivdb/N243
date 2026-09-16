---
type: PRD-MOC
version: "1.0"
date: "2026-09-16"
status: accepted
intent_hash: 0xPRD_MOC_N243_MASTER_20260916
citizen: "L4-TOOLS"
layer: "L4"
author: gerivdb
source_repo: gerivdb/N243
source_path: MOC/PRD-MOC-N243-MASTER.md
parent_doc: INTENT-Q243-NATIVE-INFERENCE-20260825
related_adr: ADR-2026-06-28-001-LOGICAL-ARCHITECTURE-N1-N4.md, ADR-2026-07-28-019-INTENT-VALIDATION-PIPELINE.md
related_intent: INTENT-Q243-NATIVE-INFERENCE-20260825
related_moc: PRD-MOC-WAZAA-MASTER.md, PRD-MOC-LLUX-MASTER.md, PRD-MOC-PIANO-MASTER.md, PRD-MOC-FLEX-MASTER.md, PRD-MOC-KG-L-MASTER.md, PRD-MOC-GOVERNANCE-HUB-MASTER.md, PRD-MOC-CROSS-REPO-DEPENDENCY-GRAPH.md, PRD-MOC-CI-CD-CROSS-REPO.md
---

# PRD-MOC — N243 Master : Orchestrateur Cognitif L*

## Résumé Exécutif

Ce MOC **MASTER** synthétise l'ensemble des PRD-MOCs N243 existants en une vue unifiée pour appréhender le rôle d'orchestrateur cognitif de N243 (L4-TOOLS). Il sert de point d'entrée unique pour comprendre l'architecture, les dépendances, l'état d'avancement et les points d'entrée opérationnels de N243.

---

## 1. Arborescence des MOCs N243

```
N243 (L4-TOOLS)
└── PRD-MOC-N243-MASTER.md                          ← CE FICHIER (MASTER)
```

**Note** : N243 est actuellement en **DRAFT 0.1.0**. Aucun MOC subalterne n'existe encore. Ce MASTER documente l'état cible et les dépendances.

---

## 2. Vue d'Ensemble Architecture N243

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              N243 (L4-TOOLS)                                │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │  WAZAA      │  │   LLUX       │  │  RLM-243    │  │   TIMX      │       │
│  │ (L4-TOOLS)  │  │ (L3-CITIZENS)│  │ (L4-TOOLS)  │  │ (SERVICES)  │       │
│  │ Bus Intent  │  │ Runner LLM   │  │ Runner RL   │  │ Runner Temp │       │
│  └──────┬──────┘  └──────┬───────┘  └──────┬──────┘  └──────┬──────┘       │
│         │               │                    │                   │          │
│         ▼               ▼                    ▼                   ▼          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    N243 CORE (L4-TOOLS)                              │   │
│  │  ┌─────────────┐ ┌──────────────┐ ┌─────────────┐ ┌────────────┐   │   │
│  │  │ orchestrator│ │ agent-runner │ │ wal-emitter │ │ bdcp       │   │   │
│  │  │ .rs         │ │ .rs          │ │ .rs         │ │ enforcer   │   │   │
│  │  └─────────────┘ └──────────────┘ └─────────────┘ └────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ▲                                            │
│                              │                                            │
│                    ┌─────────┴─────────┐                                  │
│                    │   ROOTX / TLM-CORE │                                │
│                    │ (Racines / Ternaire)│                               │
│                    └───────────────────┘                                │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Runners Cognitifs Orchestrés

| Runner | Repo | Rôle | Statut |
|---|---|---|---|
| **LLUX** | `L3-CITIZENS/LLUX` | Runner LLM BitNet 1.58b / 7B `.q243` | ✅ Opérationnel |
| **RLM-243** | `L4-TOOLS/RLM-243` | Runner Release Lifecycle | ✅ Présent |
| **TIMX** | `SERVICES/TIMX` | Runner Temporel / Features | ✅ Présent |
| **ROOTX** | `CAUSALITY-ENGINE` | Runner Racinage Symbolique | ✅ Présent |
| **TLM-CORE** | `TLM-LANG` | Runner Logique Ternaire | ✅ Présent |

---

## 4. Dépendances Externes (Cross-Repo)

| Dépendance | Repo | Rôle | Statut |
|---|---|---|---|
| **WAZAA** | `L4-TOOLS/WAZAA` | Bus événementiel Intent, WAL, EventServer | ✅ Présent |
| **LLUX** | `L3-CITIZENS/LLUX` | Runner LLM | ✅ Opérationnel |
| **RLM-243** | `L4-TOOLS/RLM-243` | Runner Release | ✅ Présent |
| **TIMX** | `SERVICES/TIMX` | Runner Temporel | ✅ Présent |
| **ROOTX** | `CAUSALITY-ENGINE` | Runner Symbolique | ✅ Présent |
| **TLM-CORE** | `TLM-LANG` | Runner Ternaire | ✅ Présent |

---

## 5. Points d'Entrée Opérationnels (Runbooks)

| Opération | Commande | Référence |
|---|---|---|
| **Build** | `cargo build` | `README.md` |
| **Run** | `cargo run` | `README.md` |
| **WAL** | `wal/ternary-wal.md` | PRD-004 |
| **BDCP** | `bdcp/enforcer.md` | PRD-005 |

---

## 6. Critères d'Acceptation Globaux (CA)

| CA | Description | Statut |
|---|---|---|
| **CA-1** | N243 compile sans erreur (`cargo build`) | ⏳ Draft |
| **CA-2** | Orchestrateur lance les 5 runners | ⏳ Draft |
| **CA-3** | WAZAA bus événementiel opérationnel | ✅ WAZAA opérationnel |
| **CA-4** | WAL append-only fonctionnel | ⏳ Draft |
| **CA-5** | BDCP enforcer actif | ⏳ Draft |

---

## 7. Points d'Attention / Risques

| Risque | Description | Mitigation |
|---|---|---|
| **DRAFT 0.1.0** | N243 non implémenté | Priorisation selon dépendances LLUX |
| **Dépendance WAZAA** | WAZAA doit être stable | CI WAZAA + tests intégration |
| **BDCP** | Mode BDCP obligatoire | `bdcp/enforcer.md` documenté |

---

## 8. Prochaines Actions (Atomic Tasks)

| Task | Description | Priorité |
|---|---|---|
| 1 | Implémenter `orchestrator.rs` (Cargo.toml, main) | HIGH |
| 2 | Implémenter `agent-runner.rs` (protocole runners) | HIGH |
| 3 | Implémenter `wal-emitter.rs` (WAL append-only) | MEDIUM |
| 4 | Implémenter `bdcp/enforcer.rs` | MEDIUM |
| 5 | Valider intégration LLUX 7B `.q243` | HIGH |
| 6 | Créer `PRD-MOC-N243-ORCHESTRATOR.md` | MEDIUM |
| 7 | Créer `PRD-MOC-N243-WAZAA-INTEGRATION.md` | MEDIUM |

---

## 9. Références Croisées Complètes

| Type | Référence |
|---|---|
| **MOCs Parents** | `PRD-MOC-LLUX-MASTER.md`, `PRD-MOC-WAZAA-MASTER.md` |
| **ADRs Liés** | `ADR-2026-06-28-001`, `ADR-2026-07-28-019`, `ADR-2026-07-28-020` |
| **INTENTs** | `INTENT-Q243-NATIVE-INFERENCE-20260825` |
| **Repos** | `gerivdb/N243`, `gerivdb/WAZAA`, `gerivdb/LLUX` |

---

**IntentHash** : 0xPRD_MOC_N243_MASTER_20260916  
**Status** : accepted  
**Date** : 2026-09-16  

---

## 10. Corrections Effectuées (TALEX Analysis)

| ID | Type | Description | Status |
|-----|------|-------------|--------|
| ERR-REF-01 | Références | `related_moc` complété avec GOVERNANCE-HUB-MASTER, CROSS-REPO-DEPENDENCY-GRAPH, CI-CD-CROSS-REPO | ✅ corrigé |
| ERR-DRIFT-01 | Drift | Cross-references vérifiées sur GOVERNANCE-HUB, LLUX, WAZAA, PIANO, FLEX, KG-L | ✅ corrigé |
| ERR-KIVA-01 | Merge | Fallback API GitHub utilisé pour merge PR #66 (WAZAA) | ✅ contourné |

---

## 11. Proof-of-Life

- [x] LLUX MASTER : commit `5331587` — docs(LLUX): update cross-repo references
- [x] N243 MASTER : commit `9f94425` — docs(N243): complete cross-repo references in MASTER
- [x] WAZAA MASTER : PR #66 mergée — docs(WAZAA): add PRD-MOC-WAZAA-MASTER.md
- [x] PIANO MASTER : commit `161402fe` — docs(PIANO): update cross-repo references
- [x] GOVERNANCE-HUB MASTER : commit `8e9ec109` — fix datetime UTC + empty collection handling
- [x] FLEX MASTER : références à jour
- [x] KG-L MASTER : références à jour
- [x] Cross-repo graph : `PRD-MOC-CROSS-REPO-DEPENDENCY-GRAPH.md` créé
- [x] CI/CD cross-repo : `PRD-MOC-CI-CD-CROSS-REPO.md` créé

---

*Dernière mise à jour : 2026-09-17T01:00:00+02:00*

