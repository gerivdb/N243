// N243 — Orchestrator
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use crate::agents::AgentRegistry;
use crate::wal::N243WAL;
use crate::workflows::{N243WorkflowRegistry, WorkflowValidator};
use crate::bdcp::N243BDCPGovernor;
use crate::bridge::{wazaa_bridge::WazaaBridge, voltx_bridge::VoltxBridge};

/// N243 orchestrator state.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum OrchestratorState {
    Idle,
    Running,
    Failed,
}

/// N243 orchestrator.
pub struct Orchestrator {
    pub state: OrchestratorState,
    pub registry: AgentRegistry,
    pub wal: N243WAL,
    pub bdcp: N243BDCPGovernor,
    pub wazaa: WazaaBridge,
    pub voltx: VoltxBridge,
    pub workflow_registry: N243WorkflowRegistry,
    pub validator: WorkflowValidator,
}

impl Orchestrator {
    /// Create a new orchestrator.
    pub fn new(wal_path: impl Into<String>) -> Self {
        Self {
            state: OrchestratorState::Idle,
            registry: AgentRegistry::new(),
            wal: N243WAL::with_path(wal_path),
            bdcp: N243BDCPGovernor::new(),
            wazaa: WazaaBridge::new(),
            voltx: VoltxBridge::new(),
            workflow_registry: N243WorkflowRegistry::new(),
            validator: WorkflowValidator::new(),
        }
    }

    /// Register the core N243 agents.
    pub fn register_core_agents(&mut self) {
        self.registry.register(
            crate::agents::Agent::new("llux", "LLUX")
                .with_capabilities(vec!["transform".into(), "index_node".into()]),
        );
        self.registry.register(
            crate::agents::Agent::new("timx", "TIMX")
                .with_capabilities(vec!["schedule_train".into(), "export_dataset".into()]),
        );
        self.registry.register(
            crate::agents::Agent::new("rootx", "ROOTX")
                .with_capabilities(vec!["analyze_causal".into(), "validate_ontology".into()]),
        );
        self.registry.register(
            crate::agents::Agent::new("tlm", "TLM")
                .with_capabilities(vec!["evaluate_ternary".into(), "detect_oscillation".into()]),
        );
        self.registry.register(
            crate::agents::Agent::new("rlm243", "RLM-243")
                .with_capabilities(vec!["plan_release".into(), "validate_stage".into()]),
        );
    }

    /// Start the orchestrator.
    pub fn start(&mut self) {
        self.state = OrchestratorState::Running;
        self.register_core_agents();
    }

    /// Stop the orchestrator.
    pub fn stop(&mut self) {
        self.state = OrchestratorState::Idle;
    }
}
