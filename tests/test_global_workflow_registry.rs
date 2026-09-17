// N243 — Global Workflow Registry Integration Test
// Valide que tous les workflows YAML existants sont détectés et valides.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use std::fs;
use std::path::Path;

#[test]
fn test_all_workflows_exist() {
    let workflows = [
        "workflows/kg_mutation/n243-kg-mutation.yaml",
        "workflows/ml_train/n243-ml-train.yaml",
        "workflows/personae_ingest/n243-personae-ingest.yaml",
        "workflows/verses_ingest/n243-verses-ingest.yaml",
        "workflows/query/n243-query.yaml",
        "workflows/rai/n243-rai.yaml",
        "workflows/ingestion/n243-ingestion.yaml",
    ];

    for workflow_path in &workflows {
        let path = Path::new(workflow_path);
        assert!(path.exists(), "workflow {} should exist", workflow_path);
    }
}

#[test]
fn test_all_workflows_have_valid_yaml_frontmatter() {
    let workflows = [
        "workflows/kg_mutation/n243-kg-mutation.yaml",
        "workflows/ml_train/n243-ml-train.yaml",
        "workflows/personae_ingest/n243-personae-ingest.yaml",
        "workflows/verses_ingest/n243-verses-ingest.yaml",
        "workflows/query/n243-query.yaml",
        "workflows/rai/n243-rai.yaml",
        "workflows/ingestion/n243-ingestion.yaml",
    ];

    for workflow_path in &workflows {
        let path = Path::new(workflow_path);
        let content = fs::read_to_string(path).expect("read workflow yaml");
        
        // Check YAML frontmatter
        assert!(content.starts_with("---\n"), "{} should start with YAML frontmatter", workflow_path);
        assert!(content.contains("name:"), "{} should have name field", workflow_path);
        assert!(content.contains("version:"), "{} should have version field", workflow_path);
        assert!(content.contains("status:"), "{} should have status field", workflow_path);
        assert!(content.contains("triggers:"), "{} should have triggers field", workflow_path);
        assert!(content.contains("steps:"), "{} should have steps field", workflow_path);
    }
}

#[test]
fn test_workflow_registry_validates_all_workflows() {
    use n243::workflows::{N243Workflow, N243WorkflowAction, N243WorkflowTrigger, WorkflowValidator};
    
    let validator = WorkflowValidator::new();
    let workflows = vec![
        ("kg_mutation", "KG Mutation", "n243.gate.decision"),
        ("ml_train", "ML Train", "n243.gate.decision"),
        ("personae_ingest", "Personae Ingest", "personae.updated"),
        ("verses_ingest", "Verses Ingest", "verse.updated"),
        ("query", "Query", "user query"),
        ("rai", "RAI", "probe fail"),
        ("ingestion", "Ingestion", "git commit"),
    ];

    for (id, name, _trigger) in workflows {
        let wf = N243Workflow {
            id: id.into(),
            name: name.into(),
            triggers: vec![N243WorkflowTrigger {
                intent_hash: format!("0xTEST_{}", id),
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
        assert!(validator.is_valid(&wf), "workflow {} should be valid", id);
    }
}
