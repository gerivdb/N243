// N243 — WAL Emitter Unit Tests
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use n243::wal_emitter::WalEmitter;
use n243::wal::{N243WAL, TernaryState};

#[test]
fn test_wal_emitter_creation() {
    let emitter = WalEmitter::new(N243WAL::new());
    assert!(emitter.history("anything").is_empty());
}

#[test]
fn test_wal_emitter_emit_convergence() {
    let mut emitter = WalEmitter::new(N243WAL::new());
    emitter.emit_convergence("entity.1", "convergence-reason");
    assert_eq!(emitter.current_state("entity.1"), Some(TernaryState::Convergence));
    assert_eq!(emitter.history("entity.1").len(), 1);
}

#[test]
fn test_wal_emitter_emit_divergence() {
    let mut emitter = WalEmitter::new(N243WAL::new());
    emitter.emit_divergence("entity.2", "divergence-reason");
    assert_eq!(emitter.current_state("entity.2"), Some(TernaryState::Divergence));
    assert_eq!(emitter.history("entity.2").len(), 1);
}

#[test]
fn test_wal_emitter_emit_oscillation() {
    let mut emitter = WalEmitter::new(N243WAL::new());
    emitter.emit_oscillation("entity.3", "oscillation-reason");
    assert_eq!(emitter.current_state("entity.3"), Some(TernaryState::Oscillation));
    assert_eq!(emitter.history("entity.3").len(), 1);
}

#[test]
fn test_wal_emitter_emit_generic() {
    let mut emitter = WalEmitter::new(N243WAL::new());
    emitter.emit("entity.4", TernaryState::Convergence, "generic-reason");
    assert_eq!(emitter.current_state("entity.4"), Some(TernaryState::Convergence));
    assert_eq!(emitter.history("entity.4").len(), 1);
}

#[test]
fn test_wal_emitter_history_tracks_multiple_events() {
    let mut emitter = WalEmitter::new(N243WAL::new());
    emitter.emit("entity.5", TernaryState::Oscillation, "first");
    emitter.emit("entity.5", TernaryState::Convergence, "second");
    emitter.emit("entity.5", TernaryState::Divergence, "third");
    assert_eq!(emitter.history("entity.5").len(), 3);
    assert_eq!(emitter.current_state("entity.5"), Some(TernaryState::Divergence));
}
