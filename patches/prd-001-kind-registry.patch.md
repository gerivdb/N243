# Patch PRD-001 — Ajout des kinds L* dans buzz-core/src/kind.rs

**Date** : 2026-08-01
**Cible** : BUZZ-X/Buzz@block/crates/buzz-core/src/kind.rs
**Statut** : DRAFT

---

## Contexte

Ajout des kinds Nostr N243 (40050-40057) dans le registre Buzz.

---

## Modifications

### 1. Ajouter les nouveaux kinds (avant les tests)

```rust
// ============================================================
// N243 — Kinds L* pour runners, ternaire, BDCP
// ============================================================

/// Kind 40050 : Runner Status — État d'un runner L*
pub const RUNNER_STATUS: u32 = 40050;

/// Kind 40051 : Runner Invocation — Invocation d'un runner
pub const RUNNER_INVOCATION: u32 = 40051;

/// Kind 40052 : Ternary Decision — Décision ternaire
pub const TERNARY_DECISION: u32 = 40052;

/// Kind 40053 : Ternary WAL — Entrée WAL ternaire
pub const TERNARY_WAL: u32 = 40053;

/// Kind 40054 : Persona-Verse — Persona-Verse invoqué
pub const PERSONA_VERSE: u32 = 40054;

/// Kind 40055 : VFT Level — Niveau VFT (fractal)
pub const VFT_LEVEL: u32 = 40055;

/// Kind 40056 : BDCP Enforcement — Événement BDCP
pub const BDCP_ENFORCEMENT: u32 = 40056;

/// Kind 40057 : Community Stratum — Strate L* d'une community
pub const COMMUNITY_STRATUM: u32 = 40057;
```

### 2. Ajouter à ALL_KINDS

Ajouter dans le tableau ALL_KINDS :
```rust
    RUNNER_STATUS,
    RUNNER_INVOCATION,
    TERNARY_DECISION,
    TERNARY_WAL,
    PERSONA_VERSE,
    VFT_LEVEL,
    BDCP_ENFORCEMENT,
    COMMUNITY_STRATUM,
```

---

## Validation

```bash
cd D:/DO/WEB/TOOLS/L4-TOOLS/BUZZ-X/Buzz@block
cargo build -p buzz-core
cargo test -p buzz-core
```

---

## Références

- **PRD-001** : N243/schemas/kinds-lstar.md
- **ADR-2026-08-01-002** : N243 Meta-Engine Architecture
