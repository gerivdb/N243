# PRD-003 — Patch Ternary Workflow Actions

> **SUPERSEDÉ (2026-08-23)** : cible Buzz@block abandonnée dans ENV2 — remplacée par **WAZAA** (moteur workflow natif `src/workflows.rs`). Réf : INTENT-2026-08-22-KG-L-WAZAA-N243-SOUVERAIN-V0_5. Document conservé pour historique — NE PAS APPLIQUER.

**Fichier** : `BUZZ-X/patches/prd-003-ternary-actions.diff`
**Appliqué à** : `Buzz@block/crates/buzz-workflow/src/ternary_actions.rs`

## Description

Ajoute les actions ternaires Approve/Suspend/Reject dans le workflow engine.

## Application

cd D:/DO/WEB/TOOLS/L4-TOOLS/BUZZ-X/Buzz@block
git apply ../patches/prd-003-ternary-actions.diff

## Références

- **PRD-003** : N243/workflows/ternary-actions.md
- **ADR-2026-08-01-002** : N243 Meta-Engine Architecture
