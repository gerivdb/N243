// N243 — Workflows
// Orchestration de workflows N243 — pont vers le bus WAZAA.

use serde::{Deserialize, Serialize};
use std::collections::HashMap;

/// Workflow trigger in N243
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct N243WorkflowTrigger {
    pub intent_hash: String,
    pub source: String,
    pub event_kind: u64,
    pub payload: serde_json::Value,
}

/// Workflow action in N243
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct N243WorkflowAction {
    pub name: String,
    pub runner: Option<String>,
    pub input: Option<String>,
    pub timeout_secs: u64,
}

/// Workflow definition in N243
#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct N243Workflow {
    pub id: String,
    pub name: String,
    pub triggers: Vec<N243WorkflowTrigger>,
    pub actions: Vec<N243WorkflowAction>,
    pub enabled: bool,
}

/// N243 Workflow Registry
#[derive(Debug, Clone, Default)]
pub struct N243WorkflowRegistry {
    workflows: HashMap<String, N243Workflow>,
}

impl N243WorkflowRegistry {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn register(&mut self, workflow: N243Workflow) {
        self.workflows.insert(workflow.id.clone(), workflow);
    }

    pub fn get(&self, id: &str) -> Option<&N243Workflow> {
        self.workflows.get(id)
    }

    pub fn list_enabled(&self) -> Vec<&N243Workflow> {
        self.workflows.values().filter(|w| w.enabled).collect()
    }

    pub fn find_by_event_kind(&self, kind: u64) -> Vec<&N243Workflow> {
        self.workflows
            .values()
            .filter(|w| {
                w.enabled
                    && w.triggers
                        .iter()
                        .any(|t| t.event_kind == kind)
            })
            .collect()
    }
}

/// Workflow validation helper for N243.
/// Validates required fields without changing existing workflow semantics.
#[derive(Debug, Clone, Default)]
pub struct WorkflowValidator;

impl WorkflowValidator {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn validate(&self, workflow: &N243Workflow) -> Vec<String> {
        let mut errors = Vec::new();
        if workflow.id.trim().is_empty() {
            errors.push("workflow.id is required".to_string());
        }
        if workflow.name.trim().is_empty() {
            errors.push("workflow.name is required".to_string());
        }
        if workflow.triggers.is_empty() {
            errors.push("workflow.triggers is required".to_string());
        }
        if workflow.actions.is_empty() {
            errors.push("workflow.actions is required".to_string());
        }
        errors
    }

    pub fn is_valid(&self, workflow: &N243Workflow) -> bool {
        self.validate(workflow).is_empty()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_n243_workflow_registry() {
        let mut registry = N243WorkflowRegistry::new();
        let wf = N243Workflow {
            id: "wf-1".to_string(),
            name: "Test Workflow".to_string(),
            triggers: vec![N243WorkflowTrigger {
                intent_hash: "0xTEST".to_string(),
                source: "wazaa-bus".to_string(),
                event_kind: 7,
                payload: serde_json::json!({"test": true}),
            }],
            actions: vec![N243WorkflowAction {
                name: "echo".to_string(),
                runner: Some("echo".to_string()),
                input: Some("hello".to_string()),
                timeout_secs: 10,
            }],
            enabled: true,
        };
        registry.register(wf);
        assert_eq!(registry.find_by_event_kind(7).len(), 1);
        assert_eq!(registry.find_by_event_kind(1).len(), 0);
    }

    #[test]
    fn test_workflow_validator_valid() {
        let validator = WorkflowValidator::new();
        let wf = N243Workflow {
            id: "wf-1".to_string(),
            name: "Test".to_string(),
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
        assert!(validator.is_valid(&wf));
        assert!(validator.validate(&wf).is_empty());
    }

    #[test]
    fn test_workflow_validator_invalid() {
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
    }
}
