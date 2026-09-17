// N243 — Ingestion Workflow Integration Test
// Validation du workflow `ingestion`.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use std::fs;
use std::path::Path;

#[test]
fn test_ingestion_workflow_file_exists() {
    let path = Path::new("workflows/ingestion/n243-ingestion.yaml");
    assert!(path.exists(), "ingestion workflow should exist");
}

#[test]
fn test_ingestion_workflow_has_required_steps() {
    let path = Path::new("workflows/ingestion/n243-ingestion.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("scan-repos"), "missing scan-repos step");
    assert!(content.contains("extract-metadata"), "missing extract-metadata step");
    assert!(content.contains("build-graph"), "missing build-graph step");
    assert!(content.contains("update-embeddings"), "missing update-embeddings step");
    assert!(content.contains("validate-mox"), "missing validate-mox step");
    assert!(content.contains("pre-impl-inventory"), "missing pre-impl-inventory step");
    assert!(content.contains("log-wal"), "missing log-wal step");
}

#[test]
fn test_ingestion_workflow_has_triggers() {
    let path = Path::new("workflows/ingestion/n243-ingestion.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("git commit"), "missing git commit trigger");
    assert!(content.contains("nightly"), "missing nightly trigger");
    assert!(content.contains("manual"), "missing manual trigger");
}
