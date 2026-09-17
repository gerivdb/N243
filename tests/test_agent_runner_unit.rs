// N243 — Agent Runner Unit Tests
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use n243::agent_runner::{AgentRunnerId, AgentRunnerRegistry};

#[test]
fn test_agent_runner_id_as_str() {
    assert_eq!(AgentRunnerId::Llux.as_str(), "llux");
    assert_eq!(AgentRunnerId::Timx.as_str(), "timx");
    assert_eq!(AgentRunnerId::Rootx.as_str(), "rootx");
    assert_eq!(AgentRunnerId::Tlm.as_str(), "tlm");
    assert_eq!(AgentRunnerId::Rlm243.as_str(), "rlm243");
}

#[test]
fn test_agent_runner_registry_creation() {
    let registry = AgentRunnerRegistry::new();
    assert!(registry.protocol_registry.get_functor(n243::gates::runner_protocol::RunnerType::LLUX).is_some());
}

#[test]
fn test_agent_runner_validate_runner() {
    use n243::gates::runner_protocol::RunnerType;
    let mut registry = AgentRunnerRegistry::new();
    let result = registry.validate_runner(AgentRunnerId::Llux);
    assert_eq!(result.runner_type, RunnerType::LLUX);
    assert!(result.gate_passed);
}

#[test]
fn test_agent_runner_workflow_registration() {
    use n243::workflows::{N243Workflow, N243WorkflowAction, N243WorkflowTrigger};
    
    let mut registry = AgentRunnerRegistry::new();
    let workflow = N243Workflow {
        id: "test-workflow".into(),
        name: "Test Workflow".into(),
        triggers: vec![N243WorkflowTrigger {
            intent_hash: "0xTEST".into(),
            source: "test".into(),
            event_kind: 1,
            payload: serde_json::json!({}),
        }],
        actions: vec![N243WorkflowAction {
            name: "test_action".into(),
            runner: None,
            input: None,
            timeout_secs: 10,
        }],
        enabled: true,
    };
    
    registry.register_workflow(workflow);
    let workflows = registry.workflows_for_event(1);
    assert_eq!(workflows.len(), 1);
    assert_eq!(workflows[0].id, "test-workflow");
}
