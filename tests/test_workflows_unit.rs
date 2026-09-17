// N243 — external unit tests for `src/workflows.rs`
// Coverage: registry filtering, disabled workflow exclusion, whitespace validation.

use n243::workflows::{N243Workflow, N243WorkflowAction, N243WorkflowTrigger, WorkflowValidator};

fn sample_workflow(id: &str, event_kind: u64, enabled: bool) -> N243Workflow {
    N243Workflow {
        id: id.to_string(),
        name: format!("Workflow {}", id),
        triggers: vec![N243WorkflowTrigger {
            intent_hash: "0xTEST".to_string(),
            source: "bus".to_string(),
            event_kind,
            payload: serde_json::json!({}),
        }],
        actions: vec![N243WorkflowAction {
            name: "act".to_string(),
            runner: None,
            input: None,
            timeout_secs: 5,
        }],
        enabled,
    }
}

#[test]
fn test_workflow_registry_list_enabled_excludes_disabled() {
    let mut registry = n243::workflows::N243WorkflowRegistry::new();
    registry.register(sample_workflow("enabled-1", 1, true));
    registry.register(sample_workflow("disabled-1", 1, false));
    registry.register(sample_workflow("enabled-2", 2, true));

    let enabled = registry.list_enabled();
    assert_eq!(enabled.len(), 2);
    let ids: Vec<&str> = enabled.iter().map(|w| w.id.as_str()).collect();
    assert!(ids.contains(&"enabled-1"));
    assert!(ids.contains(&"enabled-2"));
    assert!(!ids.contains(&"disabled-1"));
}

#[test]
fn test_workflow_registry_find_by_event_kind_ignores_disabled() {
    let mut registry = n243::workflows::N243WorkflowRegistry::new();
    registry.register(sample_workflow("active", 42, true));
    registry.register(sample_workflow("inactive", 42, false));

    let matches = registry.find_by_event_kind(42);
    assert_eq!(matches.len(), 1);
    assert_eq!(matches[0].id, "active");
}

#[test]
fn test_workflow_validator_rejects_whitespace_only_name() {
    let validator = WorkflowValidator::new();
    let workflow = N243Workflow {
        id: "wf-1".to_string(),
        name: "   ".to_string(),
        triggers: vec![N243WorkflowTrigger {
            intent_hash: "0xTEST".to_string(),
            source: "bus".to_string(),
            event_kind: 1,
            payload: serde_json::json!({}),
        }],
        actions: vec![N243WorkflowAction {
            name: "act".to_string(),
            runner: None,
            input: None,
            timeout_secs: 5,
        }],
        enabled: true,
    };
    assert!(!validator.is_valid(&workflow));
    let errors = validator.validate(&workflow);
    assert!(errors.iter().any(|e| e.contains("workflow.name is required")));
}

#[test]
fn test_workflow_registry_multiple_workflows_same_event_kind() {
    let mut registry = n243::workflows::N243WorkflowRegistry::new();
    registry.register(sample_workflow("wf-a", 7, true));
    registry.register(sample_workflow("wf-b", 7, true));
    registry.register(sample_workflow("wf-c", 7, true));

    let matches = registry.find_by_event_kind(7);
    assert_eq!(matches.len(), 3);
}

#[test]
fn test_workflow_validator_requires_triggers_and_actions() {
    let validator = WorkflowValidator::new();
    let mut workflow = sample_workflow("wf-empty", 1, true);
    workflow.triggers.clear();
    workflow.actions.clear();

    assert!(!validator.is_valid(&workflow));
    let errors = validator.validate(&workflow);
    assert!(errors.iter().any(|e| e.contains("workflow.triggers is required")));
    assert!(errors.iter().any(|e| e.contains("workflow.actions is required")));
}
