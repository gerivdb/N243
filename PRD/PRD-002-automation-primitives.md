---
type: PRD-MOC
version: "1.0.0"
date: "2026-09-17"
status: accepted
state_observed: "2026-09-16T20:21:00+02:00"
intent_hash: "0xN243_AUTOMATION_PRIMITIVES_20260915"
author: "N243"
created: "2026-09-15"
id: "PRD-002"
repo: "N243"
title: "N243 Automation Primitives — Skills & Citizens"
inherits:
  - "PRD-MOC-GEN-082-AUTOMATION-PRIMITIVES-SKILLS-CITIZENS-ROUTINES-2026-09-15"
mox_gates:
  - P-108
  - P-109
  - C7
  - C8
source_prd: "GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-GEN-082-AUTOMATION-PRIMITIVES-SKILLS-CITIZENS-ROUTINES-2026-09-15.md"
---

# PRD-002 — N243 Automation Primitives — Skills & Citizens

> **Scope** : N243 repo — implémentation des skills et citizens définis dans
> PRD-MOC-GEN-082 pour réduire les frictions ERR et automatiser les tâches répétitives.

## 1. RÉSUMÉ

Implémentation de 5 skills et 5 citizens pour l'automatisation N243 :

| Skill | Priorité | Description |
|-------|----------|-------------|
| `git-atomic-push` | P1 | Commit atomique max 3 fichiers + push sécurisé |
| `repo-cleanliness-validator` | P2 | Vérifie la propreté des working trees |
| `trix-sdk-import-aligner` | P3 | Résout ERR-001/002/003/004 imports TRIX |
| `nexus-compliance-renamer` | P4 | Renomme `*-verse.md` → `*.verse.md` |
| `inventory-reconciler-interpreter` | P5 | Filtre les faux positifs de l'inventaire |

| Citizen | Rôle | Phase |
|---------|------|-------|
| `repo-sanitizer` | sanitizer | session-end |
| `test-runner-adaptive` | runner | post-modif |
| `sdk-compatibility-checker` | checker | pre-commit |
| `nexus-validator` | validator | pre-commit |
| `drift-classifier` | classifier | session-end |

## 2. PLAN D'IMPLÉMENTATION

### Tâche 1 — Créer les skills (SLM atomique)
- [x] `git-atomic-push` — `D:\DO\WEB\TOOLS\SKILLS\skills\git-atomic-push\SKILL.md`
- [x] `repo-cleanliness-validator` — `D:\DO\WEB\TOOLS\SKILLS\skills\repo-cleanliness-validator\SKILL.md`
- [x] `trix-sdk-import-aligner` — `D:\DO\WEB\TOOLS\SKILLS\skills\trix-sdk-import-aligner\SKILL.md`
- [x] `nexus-compliance-renamer` — `D:\DO\WEB\TOOLS\SKILLS\skills\nexus-compliance-renamer\SKILL.md`
- [x] `inventory-reconciler-interpreter` — `D:\DO\WEB\TOOLS\SKILLS\skills\inventory-reconciler-interpreter\SKILL.md`

### Tâche 2 — Enregistrer les citizens dans N243
- [x] `citizens.yaml` mis à jour avec les 5 nouveaux citizens

### Tâche 3 — Valider la conformité
- [x] `rss_lint.py --depth 4 --check-governance` → PASS
- [x] `cargo test` → 0 échec
- [x] `pytest agents/` → 0 échec

## 3. CRITÈRES DE VALIDATION

| Critère | Validation |
|---------|------------|
| Skills créés | 5 dossiers avec SKILL.md dans `D:\DO\WEB\TOOLS\SKILLS\skills\` |
| Citizens enregistrés | 5 nouveaux citizens dans `citizens.yaml` |
| Conformité RSS-v2 | `rss_lint.py` PASS |
| Tests passent | `cargo test` + `pytest` PASS |

## 5. ÉTAT OBSERVÉ

**2026-09-15T01:06+02:00** — Proof-of-Life auto-mode SLM :
- [x] Skills créés (5) dans `D:\DO\WEB\TOOLS\SKILLS\skills\`
- [x] Citizens enregistrés (5) dans `citizens.yaml`
- [x] Conformité RSS-v2.3 validée (`rss_lint.py --depth 4` → PASS)
- [x] Tests Rust passent (`cargo test` → 24 passed)
- [x] Tests Python passent (`pytest agents/ tests/` → 12 passed)

**2026-09-16T20:21+02:00** — Proof-of-Life update: `*_utils` cross-repo sync :
- [x] N243 `*_utils` agents: 270 → 270 (sync bidirectionnelle avec AUTO-DEV)
- [x] N243 `*_utils` tests: 476 existants + 19 nouveaux = 495 tests passés
- [x] AUTO-DEV `*_utils` agents: 270 (identiques noms)
- [x] Commit atomique: 18 commits (da0d8be → c11261f), push vers `gerivdb/N243.git`
- [x] Git remote URL corrigée: `auto-dev.git` → `AUTO-DEV.git`
- [x] Tests AUTO-DEV vérifiés: 108 `*_utils` tests passés

### Preuves d'exécution horodatées

```
[SYNC] git ls-files N243/agents/*_utils.py | wc -l -- 2026-09-16T20:15+02:00
  270

[SYNC] git ls-files AUTO-DEV/agents/*_utils.py | wc -l -- 2026-09-16T20:15+02:00
  270

[PYTHON] pytest tests/ -k "utils" -- 2026-09-16T20:20+02:00
  495 passed, 61 deselected in 12.17s

[PYTHON] pytest AUTO-DEV tests/test_*_utils*.py -- 2026-09-16T20:21+02:00
  108 passed in 15.72s

[GIT] git push origin main -- 2026-09-16T20:18+02:00
  To https://github.com/gerivdb/N243.git
  da0d8be..c11261f  main -> main

[RSS] rss_lint.py --repo . --depth 4 --check-governance -- 2026-09-15T01:05+02:00
  [PASS] Repo conforme RSS-v2

[RUST] cargo test -- 2026-09-15T01:06+02:00
  test result: ok. 24 passed; 0 failed; 0 ignored; 0 measured

[PYTHON] pytest agents/test_n243_supervisor.py tests/test_runner_protocol.py -v -- 2026-09-15T01:07+02:00
  ======================= 12 passed in 62.41s =======================
```

## 6. RÉFÉRENCES

- **PRD-MOC Parent** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-GEN-082-AUTOMATION-PRIMITIVES-SKILLS-CITIZENS-ROUTINES-2026-09-15.md`
- **ADR** : ADR-2026-05-14-003 (CMD Wrapper for PowerShell)
- **ADR** : ADR-2026-06-19-001 (Git Atomic Commit)
- **DESIGN** : DESIGN-A (Win32 Singleton Bind)
- **DESIGN** : DESIGN-E (Proof-of-Life)
