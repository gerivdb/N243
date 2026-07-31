# PRD-004 - Ternary WAL

**Version** : 1.0
**Statut** : DRAFT
**IntentHash** : 0xPRD004_20260801
**ADR lie** : ADR-2026-08-01-002-n243-meta-engine.md

---

## 1. Contexte

WAL ternaire avec 3 etats :
- **CONVERGENCE** (1.0) - succes
- **DIVERGENCE** (0.0) - echec
- **OSCILLATION** (0.5) - instable

---

## 2. Structure

```rust
pub enum TernaryState {
    Convergence,
    Divergence,
    Oscillation,
}

pub struct TernaryWALEntry {
    pub id: Uuid,
    pub timestamp: i64,
    pub entity: String,
    pub previous: TernaryState,
    pub current: TernaryState,
    pub reason: String,
}
```

---

## 3. Transitions

CONVERGENCE -> DIVERGENCE : Echec
CONVERGENCE -> OSCILLATION : Instabilite
DIVERGENCE -> CONVERGENCE : Recuperation
OSCILLATION -> CONVERGENCE : Stabilisation
OSCILLATION -> DIVERGENCE : Echec confirme

---

## 4. Oscillation Detection

```yaml
oscillation_detection:
  max_transitions: 5
  window_secs: 300
  action: "alert"
```

---

## 5. Validation

| Check | Commande |
|-------|----------|
| State machine | Tests transitions |
| Nostr events | Kind 40053 |

---

## 6. References

- **buzz-audit** : `crates/buzz-audit/src/lib.rs`
- **PRD-001** : Event Schema
