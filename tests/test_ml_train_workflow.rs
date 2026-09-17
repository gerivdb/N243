// N243 — ML Train Workflow Integration Test
// Validation du workflow `ml_train`.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use std::fs;
use std::path::Path;

#[test]
fn test_ml_train_workflow_file_exists() {
    let path = Path::new("workflows/ml_train/n243-ml-train.yaml");
    assert!(path.exists(), "ml_train workflow should exist");
}

#[test]
fn test_ml_train_workflow_has_required_steps() {
    let path = Path::new("workflows/ml_train/n243-ml-train.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("receive_trigger"), "missing receive_trigger step");
    assert!(content.contains("validate_gf"), "missing validate_gf step");
    assert!(content.contains("export_dataset"), "missing export_dataset step");
    assert!(content.contains("schedule_train"), "missing schedule_train step");
    assert!(content.contains("run_training"), "missing run_training step");
    assert!(content.contains("evaluate_model"), "missing evaluate_model step");
    assert!(content.contains("log_wal"), "missing log_wal step");
    assert!(content.contains("publish_wazaa"), "missing publish_wazaa step");
}

#[test]
fn test_ml_train_publishes_wazaa_topic() {
    let path = Path::new("workflows/ml_train/n243-ml-train.yaml");
    let content = fs::read_to_string(path).expect("read workflow yaml");
    assert!(content.contains("kg-l.ml.train"), "missing kg-l.ml.train topic");
    assert!(content.contains("model_id:"), "missing model_id in payload");
}
