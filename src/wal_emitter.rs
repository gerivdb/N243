// N243 — WAL Emitter
// Couche d'émission append-only au-dessus du WAL existant.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use crate::wal::{N243WAL, TernaryState, WalEntry};

/// WAL emitter for N243.
/// Provides append-only emission of governance and runtime events.
pub struct WalEmitter {
    wal: N243WAL,
}

impl WalEmitter {
    /// Create a new WAL emitter.
    pub fn new(wal: N243WAL) -> Self {
        Self { wal }
    }

    /// Emit a ternary state transition.
    pub fn emit(&mut self, entity: impl Into<String>, state: TernaryState, reason: impl Into<String>) {
        self.wal.record(&entity.into(), state, &reason.into());
    }

    /// Emit a convergence event.
    pub fn emit_convergence(&mut self, entity: impl Into<String>, reason: impl Into<String>) {
        self.emit(entity, TernaryState::Convergence, reason);
    }

    /// Emit a divergence event.
    pub fn emit_divergence(&mut self, entity: impl Into<String>, reason: impl Into<String>) {
        self.emit(entity, TernaryState::Divergence, reason);
    }

    /// Emit an oscillation event.
    pub fn emit_oscillation(&mut self, entity: impl Into<String>, reason: impl Into<String>) {
        self.emit(entity, TernaryState::Oscillation, reason);
    }

    /// Get the current state of an entity.
    pub fn current_state(&self, entity: &str) -> Option<TernaryState> {
        self.wal.current_state(entity).copied()
    }

    /// Get the history of an entity.
    pub fn history(&self, entity: &str) -> Vec<&WalEntry> {
        self.wal.history(entity)
    }
}

impl Default for WalEmitter {
    fn default() -> Self {
        Self::new(N243WAL::new())
    }
}
