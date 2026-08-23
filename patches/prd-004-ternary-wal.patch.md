# PRD-004 — Patch Ternary WAL

> **SUPERSEDÉ (2026-08-23)** : cible Buzz@block abandonnée dans ENV2 — remplacée par **WAZAA** (`wal_event_emitter.py`, JSONL append-only). Réf : INTENT-2026-08-22-KG-L-WAZAA-N243-SOUVERAIN-V0_5. Document conservé pour historique — NE PAS APPLIQUER.

**Fichier** : `BUZZ-X/patches/prd-004-ternary-wal.diff`
**Appliqué à** : `Buzz@block/crates/buzz-audit/src/ternary_wal.rs`

## Description

Ajoute le WAL ternaire avec les états Convergence/Divergence/Oscillation.

## Application

cd D:/DO/WEB/TOOLS/L4-TOOLS/BUZZ-X/Buzz@block
git apply ../patches/prd-004-ternary-wal.diff

## Références

- **PRD-004** : N243/wal/ternary-wal.md
- **ADR-2026-08-01-002** : N243 Meta-Engine Architecture
