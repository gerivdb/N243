# PRD-005 — Patch BDCP Enforcement

> **SUPERSEDÉ (2026-08-23)** : cible Buzz@block abandonnée dans ENV2 — remplacée par **WAZAA** + enforcement natif `src/bdcp.rs`. Réf : INTENT-2026-08-22-KG-L-WAZAA-N243-SOUVERAIN-V0_5. Document conservé pour historique — NE PAS APPLIQUER.

**Fichier** : `BUZZ-X/patches/prd-005-bdcp-enforcement.diff`
**Appliqué à** : `Buzz@block/crates/buzz-auth/src/bdcp.rs`

## Description

Ajoute le checker BDCP pour valider les clones contre known_repositories.yaml.

## Application

cd D:/DO/WEB/TOOLS/L4-TOOLS/BUZZ-X/Buzz@block
git apply ../patches/prd-005-bdcp-enforcement.diff

## Références

- **PRD-005** : N243/bdcp/enforcer.md
- **ADR-032** : Clone Governance
