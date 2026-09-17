// N243 — Personae Ingest Workflow Integration Test
// Validation du workflow `personae_ingest`.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use std::fs;
use std::path::Path;

#[test]
fn test_personae_ingest_workflow_file_exists() {
    let path = Path::new("workflows/personae_ingest/n243-personae-ingest.yaml");
    assert!(path.exists(), "personae_ingest workflow should exist");
}

#[test]
fn test_personae_ingest_workflow_has_required_steps() {
    let path = Path::new("workflows/personae_ingest/n243-personae-ingest.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("receive_trigger"), "missing receive_trigger step");
    assert!(content.contains("validate_gf"), "missing validate_gf step");
    assert!(content.contains("load_personae"), "missing load_personae step");
    assert!(content.contains("map_to_kg_l"), "missing map_to_kg_l step");
    assert!(content.contains("create_edges"), "missing create_edges step");
    assert!(content.contains("log_wal"), "missing log_wal step");
    assert!(content.contains("publish_wazaa"), "missing publish_wazaa step");
}

#[test]
fn test_personae_ingest_publishes_wazaa_topic() {
    let path = Path::new("workflows/personae_ingest/n243-personae-ingest.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("personae.updated"), "missing personae.updated topic");
    assert!(content.contains("personae_count: 7"), "missing personae_count in payload");
}
