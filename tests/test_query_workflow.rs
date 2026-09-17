// N243 — Query Workflow Integration Test
// Validation du workflow `query`.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use std::fs;
use std::path::Path;

#[test]
fn test_query_workflow_file_exists() {
    let path = Path::new("workflows/query/n243-query.yaml");
    assert!(path.exists(), "query workflow should exist");
}

#[test]
fn test_query_workflow_has_required_steps() {
    let path = Path::new("workflows/query/n243-query.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("validate-query"), "missing validate-query step");
    assert!(content.contains("check-cache"), "missing check-cache step");
    assert!(content.contains("execute-tql"), "missing execute-tql step");
    assert!(content.contains("format-result"), "missing format-result step");
    assert!(content.contains("validate-mox"), "missing validate-mox step");
    assert!(content.contains("pre-impl-inventory"), "missing pre-impl-inventory step");
    assert!(content.contains("log-wal"), "missing log-wal step");
}

#[test]
fn test_query_workflow_has_triggers() {
    let path = Path::new("workflows/query/n243-query.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("user query"), "missing user query trigger");
    assert!(content.contains("auto-dev probe"), "missing auto-dev probe trigger");
    assert!(content.contains("MOX validation"), "missing MOX validation trigger");
}
