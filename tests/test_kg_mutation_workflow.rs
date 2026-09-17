// N243 — KG Mutation Workflow Integration Test
// Validation du workflow `kg_mutation`.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use std::fs;
use std::path::Path;

#[test]
fn test_kg_mutation_workflow_file_exists() {
    let path = Path::new("workflows/kg_mutation/n243-kg-mutation.yaml");
    assert!(path.exists(), "kg_mutation workflow should exist");
}

#[test]
fn test_kg_mutation_workflow_has_required_steps() {
    let path = Path::new("workflows/kg_mutation/n243-kg-mutation.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("receive_decision"), "missing receive_decision step");
    assert!(content.contains("validate_gf"), "missing validate_gf step");
    assert!(content.contains("mutate_kg_l"), "missing mutate_kg_l step");
    assert!(content.contains("log_wal"), "missing log_wal step");
    assert!(content.contains("publish_wazaa"), "missing publish_wazaa step");
}

#[test]
fn test_kg_mutation_publishes_wazaa_topic() {
    let path = Path::new("workflows/kg_mutation/n243-kg-mutation.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("n243.gate.decision"), "missing n243.gate.decision trigger");
    assert!(content.contains("wazaa.event"), "missing wazaa.event trigger");
}
