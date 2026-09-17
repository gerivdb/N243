// N243 — RAI Workflow Integration Test
// Validation du workflow `rai`.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use std::fs;
use std::path::Path;

#[test]
fn test_rai_workflow_file_exists() {
    let path = Path::new("workflows/rai/n243-rai.yaml");
    assert!(path.exists(), "rai workflow should exist");
}

#[test]
fn test_rai_workflow_has_required_steps() {
    let path = Path::new("workflows/rai/n243-rai.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("run-probes"), "missing run-probes step");
    assert!(content.contains("mine-logs"), "missing mine-logs step");
    assert!(content.contains("edit-prd"), "missing edit-prd step");
    assert!(content.contains("validate-mox"), "missing validate-mox step");
    assert!(content.contains("pre-impl-inventory"), "missing pre-impl-inventory step");
    assert!(content.contains("flux-d4-gate"), "missing flux-d4-gate step");
    assert!(content.contains("log-wal"), "missing log-wal step");
}

#[test]
fn test_rai_workflow_has_triggers() {
    let path = Path::new("workflows/rai/n243-rai.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("probe fail"), "missing probe fail trigger");
    assert!(content.contains("daily"), "missing daily trigger");
    assert!(content.contains("manual"), "missing manual trigger");
}
