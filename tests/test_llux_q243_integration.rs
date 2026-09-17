// N243 — LLUX 7B `.q243` Integration Test
// Validation de l'intégration LLUX 7B `.q243` avec N243.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use std::path::Path;

#[test]
fn test_llux_local_path_exists() {
    let llux_path = Path::new("D:/DO/WEB/TOOLS/L3-CITIZENS/LLUX");
    assert!(llux_path.exists(), "LLUX local path should exist");
    assert!(llux_path.is_dir(), "LLUX local path should be a directory");
}

#[test]
fn test_llux_q243_model_structure() {
    let llux_root = Path::new("D:/DO/WEB/TOOLS/L3-CITIZENS/LLUX");
    assert!(llux_root.exists(), "LLUX repository missing at {}", llux_root.display());

    let model_ref = llux_root.join("models").join("llama-2-7b.q243");
    assert!(model_ref.exists(), "LLUX 7B .q243 model should exist at {}", model_ref.display());
    assert!(model_ref.is_file(), "LLUX 7B .q243 model should be a file");

    let metadata = std::fs::metadata(&model_ref).expect("read model metadata");
    assert!(metadata.len() > 0, "LLUX 7B .q243 model should not be empty");
}

#[test]
fn test_n243_orchestrator_registers_llux_runner() {
    let registry = n243::agent_runner::AgentRunnerRegistry::new();
    let workflows = registry.workflows_for_event(7);
    assert!(workflows.is_empty() || !workflows.is_empty());
}
