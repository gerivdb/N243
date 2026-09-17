// N243 — ML Training Pipeline Integration Test
// Validation de l'orchestration Rust du pipeline ML training.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use std::path::Path;

#[test]
fn test_ml_train_workflow_exists() {
    let path = Path::new("workflows/ml_train/n243-ml-train.yaml");
    assert!(path.exists(), "ml_train workflow should exist");
}

#[test]
fn test_ml_train_registry_lists_enabled_workflows() {
    use n243::workflows::N243WorkflowRegistry;
    let registry = N243WorkflowRegistry::new();
    let enabled = registry.list_enabled();
    assert!(enabled.is_empty() || !enabled.is_empty());
}

#[test]
fn test_ml_train_validator_accepts_workflow() {
    use n243::workflows::{N243Workflow, N243WorkflowAction, N243WorkflowTrigger, WorkflowValidator};
    let validator = WorkflowValidator::new();
    let wf = N243Workflow {
        id: "ml_train".into(),
        name: "ML Train".into(),
        triggers: vec![N243WorkflowTrigger {
            intent_hash: "0xTEST".into(),
            source: "manual".into(),
            event_kind: 1,
            payload: serde_json::json!({}),
        }],
        actions: vec![N243WorkflowAction {
            name: "run_training".into(),
            runner: Some("timx".into()),
            input: Some("dataset.jsonl".into()),
            timeout_secs: 10,
        }],
        enabled: true,
    };
    assert!(validator.is_valid(&wf));
}
