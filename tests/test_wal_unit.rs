// N243 — external unit tests for `src/wal.rs`
// Coverage: multi-entity history, current_state absence, oscillation edge cases.

use n243::wal::{N243WAL, TernaryState};

#[test]
fn test_wal_record_multiple_entities() {
    let mut wal = N243WAL::new();
    wal.record("a", TernaryState::Convergence, "");
    wal.record("b", TernaryState::Oscillation, "");
    wal.record("c", TernaryState::Divergence, "");

    assert_eq!(wal.current_state("a"), Some(&TernaryState::Convergence));
    assert_eq!(wal.current_state("b"), Some(&TernaryState::Oscillation));
    assert_eq!(wal.current_state("c"), Some(&TernaryState::Divergence));
    assert_eq!(wal.history("a").len(), 1);
    assert_eq!(wal.history("b").len(), 1);
    assert_eq!(wal.history("c").len(), 1);
}

#[test]
fn test_wal_history_returns_sorted_entries() {
    let mut wal = N243WAL::new();
    wal.record("x", TernaryState::Convergence, "");
    wal.record("x", TernaryState::Oscillation, "");
    wal.record("x", TernaryState::Divergence, "");

    let history = wal.history("x");
    assert_eq!(history.len(), 3);
    assert_eq!(history[0].current, TernaryState::Convergence);
    assert_eq!(history[1].current, TernaryState::Oscillation);
    assert_eq!(history[2].current, TernaryState::Divergence);
}

#[test]
fn test_wal_detect_oscillations_multiple_transitions() {
    let mut wal = N243WAL::new();
    wal.record("x", TernaryState::Convergence, "");
    wal.record("x", TernaryState::Oscillation, "");
    wal.record("x", TernaryState::Divergence, "");
    wal.record("x", TernaryState::Oscillation, "");
    wal.record("x", TernaryState::Convergence, "");

    let oscillations = wal.detect_oscillations("x");
    assert_eq!(oscillations.len(), 4);
}

#[test]
fn test_wal_current_state_returns_none_for_unknown() {
    let wal = N243WAL::new();
    assert!(wal.current_state("unknown").is_none());
}

#[test]
fn test_wal_with_path_appends_to_file() {
    let tmp = std::env::temp_dir().join("n243-wal-path-test.jsonl");
    let _ = std::fs::remove_file(&tmp);

    let mut wal = N243WAL::with_path(tmp.to_str().unwrap());
    wal.record("e1", TernaryState::Convergence, "start");
    wal.record("e1", TernaryState::Oscillation, "drift");

    let content = std::fs::read_to_string(&tmp).expect("read wal file");
    let lines: Vec<&str> = content.lines().collect();
    assert_eq!(lines.len(), 2);

    let first: serde_json::Value =
        serde_json::from_str(lines[0]).expect("parse first line");
    assert_eq!(first["entity"], "e1");
    assert_eq!(first["current"], "Convergence");

    let second: serde_json::Value =
        serde_json::from_str(lines[1]).expect("parse second line");
    assert_eq!(second["current"], "Oscillation");

    let _ = std::fs::remove_file(&tmp);
}
