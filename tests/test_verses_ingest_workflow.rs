// N243 — Verses Ingest Workflow Integration Test
// Validation du workflow `verses_ingest`.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use std::fs;
use std::path::Path;

#[test]
fn test_verses_ingest_workflow_file_exists() {
    let path = Path::new("workflows/verses_ingest/n243-verses-ingest.yaml");
    assert!(path.exists(), "verses_ingest workflow should exist");
}

#[test]
fn test_verses_ingest_workflow_has_required_steps() {
    let path = Path::new("workflows/verses_ingest/n243-verses-ingest.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("receive_trigger"), "missing receive_trigger step");
    assert!(content.contains("validate_gf"), "missing validate_gf step");
    assert!(content.contains("load_verses"), "missing load_verses step");
    assert!(content.contains("validate_ontology"), "missing validate_ontology step");
    assert!(content.contains("index_kg_l"), "missing index_kg_l step");
    assert!(content.contains("log_wal"), "missing log_wal step");
    assert!(content.contains("publish_wazaa"), "missing publish_wazaa step");
}

#[test]
fn test_verses_ingest_publishes_wazaa_topic() {
    let path = Path::new("workflows/verses_ingest/n243-verses-ingest.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("verse.updated"), "missing verse.updated topic");
    assert!(content.contains("verses_count:"), "missing verses_count in payload");
}
