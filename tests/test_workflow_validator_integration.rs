// N243 — Integration tests for WorkflowValidator
// IntentHash: 0xN243_WORKFLOW_VALIDATOR_INTEGRATION_20260915

use n243::workflows::{N243Workflow, N243WorkflowAction, N243WorkflowTrigger, WorkflowValidator};

#[test]
fn test_workflow_validator_integration_valid() {
    let validator = WorkflowValidator::new();
    let wf = N243Workflow {
        id: "wf-valid".to_string(),
        name: "Valid Workflow".to_string(),
        triggers: vec![N243WorkflowTrigger {
            intent_hash: "0xVALID".to_string(),
            source: "test-bus".to_string(),
            event_kind: 1,
            payload: serde_json::json!({"test": true}),
        }],
        actions: vec![N243WorkflowAction {
            name: "test-action".to_string(),
            runner: Some("test-runner".to_string()),
            input: Some("test-input".to_string()),
            timeout_secs: 10,
        }],
        enabled: true,
    };
    assert!(validator.is_valid(&wf));
    assert!(validator.validate(&wf).is_empty());
}

#[test]
fn test_workflow_validator_integration_invalid() {
    let validator = WorkflowValidator::new();
    let wf = N243Workflow {
        id: "".to_string(),
        name: "".to_string(),
        triggers: vec![],
        actions: vec![],
        enabled: false,
    };
    assert!(!validator.is_valid(&wf));
    let errors = validator.validate(&wf);
    assert_eq!(errors.len(), 4);
    assert!(errors.contains(&"workflow.id is required".to_string()));
    assert!(errors.contains(&"workflow.name is required".to_string()));
    assert!(errors.contains(&"workflow.triggers is required".to_string()));
    assert!(errors.contains(&"workflow.actions is required".to_string()));
}
