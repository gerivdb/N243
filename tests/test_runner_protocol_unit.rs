// N243 — external unit tests for `src/gates/runner_protocol.rs`
// Coverage: RunnerType mapping, registry initialization, channel constants.

use n243::gates::runner_protocol::{RunnerProtocolRegistry, RunnerType};

#[test]
fn test_runner_type_as_str_mapping() {
    assert_eq!(RunnerType::LLUX.as_str(), "LLUX");
    assert_eq!(RunnerType::RLM243.as_str(), "RLM-243");
    assert_eq!(RunnerType::TIMX.as_str(), "TIMX");
    assert_eq!(RunnerType::ROOTX.as_str(), "ROOTX");
    assert_eq!(RunnerType::TLMCore.as_str(), "TLM-CORE");
}

#[test]
fn test_runner_type_all_contains_five_runners() {
    let all = RunnerType::all();
    assert_eq!(all.len(), 5);
    assert!(all.contains(&RunnerType::LLUX));
    assert!(all.contains(&RunnerType::RLM243));
    assert!(all.contains(&RunnerType::TIMX));
    assert!(all.contains(&RunnerType::ROOTX));
    assert!(all.contains(&RunnerType::TLMCore));
}

#[test]
fn test_runner_protocol_functor_creation() {
    let registry = RunnerProtocolRegistry::new();
    let functor = registry.get_functor(RunnerType::TIMX).expect("functor exists");

    assert_eq!(functor.runner_type, RunnerType::TIMX);
    assert_eq!(functor.source_verse, "N243");
    assert_eq!(functor.target_verse, "TIMX");
    assert!(functor.name.contains("TIMX"));
}

#[test]
fn test_runner_protocol_registry_has_five_functors() {
    let registry = RunnerProtocolRegistry::new();
    for runner in RunnerType::all() {
        assert!(registry.get_functor(runner).is_some());
    }
}

#[test]
fn test_runner_protocol_channels_constants() {
    use n243::gates::runner_protocol::channels;
    assert_eq!(
        channels::RUNNER_PROTOCOL,
        "L4-TOOLS/N243/runners/protocol"
    );
    assert_eq!(
        channels::RUNNER_STATE,
        "L4-TOOLS/N243/runners/state/*"
    );
    assert_eq!(
        channels::RUNNER_CLUSTER_TOPOLOGY,
        "L4-TOOLS/N243/runners/cluster"
    );
    assert_eq!(channels::RUNNER_PROTOCOL_EVENT, "RUNNER_PROTOCOL");
    assert_eq!(channels::RUNNER_STATE_EVENT, "RUNNER_STATE");
    assert_eq!(channels::RUNNER_CLUSTER_EVENT, "RUNNER_CLUSTER_TOPOLOGY");
}
