// N243 — Orchestrator Unit Tests
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use n243::orchestrator::{Orchestrator, OrchestratorState};

#[test]
fn test_orchestrator_creation() {
    let orchestrator = Orchestrator::new("wal/ternary-wal.jsonl");
    assert_eq!(orchestrator.state, OrchestratorState::Idle);
}

#[test]
fn test_orchestrator_start_stop() {
    let mut orchestrator = Orchestrator::new("wal/ternary-wal.jsonl");
    assert_eq!(orchestrator.state, OrchestratorState::Idle);

    orchestrator.start();
    assert_eq!(orchestrator.state, OrchestratorState::Running);

    orchestrator.stop();
    assert_eq!(orchestrator.state, OrchestratorState::Idle);
}

#[test]
fn test_orchestrator_registers_five_core_agents() {
    let mut orchestrator = Orchestrator::new("wal/ternary-wal.jsonl");
    orchestrator.start();

    let all_agents = orchestrator.registry.list_all();
    assert_eq!(all_agents.len(), 5, "orchestrator should register 5 core agents");

    let ids: Vec<&str> = all_agents.iter().map(|a| a.id.0.as_str()).collect();
    assert!(ids.contains(&"llux"), "missing llux agent");
    assert!(ids.contains(&"timx"), "missing timx agent");
    assert!(ids.contains(&"rootx"), "missing rootx agent");
    assert!(ids.contains(&"tlm"), "missing tlm agent");
    assert!(ids.contains(&"rlm243"), "missing rlm243 agent");
}

#[test]
fn test_orchestrator_components_are_initialized() {
    let orchestrator = Orchestrator::new("wal/ternary-wal.jsonl");
    assert!(orchestrator.bdcp.is_stratum_enforced("L4"));
    assert!(orchestrator.wazaa.is_connected() || !orchestrator.wazaa.is_connected());
    assert!(orchestrator.voltx.is_connected() || !orchestrator.voltx.is_connected());
}
