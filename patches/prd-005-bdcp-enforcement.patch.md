# PRD-005 — Patch BDCP Enforcement

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
