// N243 — external unit tests for `src/orchestrator.rs`
// Coverage: state transitions, core agent registration, empty-start invariants.

use n243::orchestrator::Orchestrator;

#[test]
fn test_orchestrator_new_starts_idle() {
    let orch = Orchestrator::new("/tmp/n243-orchestrator-test.jsonl");
    assert_eq!(orch.state, n243::orchestrator::OrchestratorState::Idle);
}

#[test]
fn test_orchestrator_start_transitions_to_running() {
    let mut orch = Orchestrator::new("/tmp/n243-orchestrator-test.jsonl");
    orch.start();
    assert_eq!(
        orch.state,
        n243::orchestrator::OrchestratorState::Running
    );
}

#[test]
fn test_orchestrator_stop_returns_to_idle() {
    let mut orch = Orchestrator::new("/tmp/n243-orchestrator-test.jsonl");
    orch.start();
    orch.stop();
    assert_eq!(orch.state, n243::orchestrator::OrchestratorState::Idle);
}

#[test]
fn test_orchestrator_start_registers_five_core_agents() {
    let mut orch = Orchestrator::new("/tmp/n243-orchestrator-test.jsonl");
    orch.start();
    let all = orch.registry.list_all();
    assert_eq!(all.len(), 5);

    let ids: Vec<String> = all.iter().map(|a| a.id.0.clone()).collect();
    assert!(ids.contains(&"llux".to_string()));
    assert!(ids.contains(&"timx".to_string()));
    assert!(ids.contains(&"rootx".to_string()));
    assert!(ids.contains(&"tlm".to_string()));
    assert!(ids.contains(&"rlm243".to_string()));
}

#[test]
fn test_orchestrator_new_has_empty_registry_and_workflows() {
    let orch = Orchestrator::new("/tmp/n243-orchestrator-test.jsonl");
    assert!(orch.registry.list_all().is_empty());
    assert!(orch.workflow_registry.list_enabled().is_empty());
    assert!(!orch.bdcp.is_stratum_enforced("L9"));
}
