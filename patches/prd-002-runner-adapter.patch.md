# PRD-002 — Patch Runner Adapter

> **SUPERSEDÉ (2026-08-23)** : cible Buzz@block abandonnée dans ENV2 — remplacée par **WAZAA** (bus Intent, adapter N243). Réf : INTENT-2026-08-22-KG-L-WAZAA-N243-SOUVERAIN-V0_5. Document conservé pour historique — NE PAS APPLIQUER.

**Fichier** : `BUZZ-X/patches/prd-002-runner-adapter.diff`
**Appliqué à** : `Buzz@block/crates/buzz-acp/src/runner_adapter.rs`

## Description

Ajoute le Runner Adapter pour invoquer les runners L* (LLUX, RLM-243, TIMX, ROOTX, TLM-CORE) via ACP.

## Application

cd D:/DO/WEB/TOOLS/L4-TOOLS/BUZZ-X/Buzz@block
git apply ../patches/prd-002-runner-adapter.diff

## Références

- **PRD-002** : N243/agents/runner-protocol.md
- **ADR-2026-08-01-002** : N243 Meta-Engine Architecture
