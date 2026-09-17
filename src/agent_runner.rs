// N243 — Agent Runner
// Protocole d'orchestration des runners L*.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use crate::agents::AgentStatus;
use crate::workflows::{N243Workflow, N243WorkflowRegistry};
use crate::gates::runner_protocol::{RunnerProtocolRegistry, RunnerProtocolResult, RunnerType};

/// Runner identifier exposed by the agent runner layer.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum AgentRunnerId {
    Llux,
    Timx,
    Rootx,
    Tlm,
    Rlm243,
}

impl AgentRunnerId {
    pub fn as_str(self) -> &'static str {
        match self {
            AgentRunnerId::Llux => "llux",
            AgentRunnerId::Timx => "timx",
            AgentRunnerId::Rootx => "rootx",
            AgentRunnerId::Tlm => "tlm",
            AgentRunnerId::Rlm243 => "rlm243",
        }
    }
}

/// Result of an agent runner execution.
#[derive(Debug, Clone)]
pub struct AgentRunnerResult {
    pub runner_id: AgentRunnerId,
    pub status: AgentStatus,
    pub output: String,
}

/// Agent runner registry for N243.
pub struct AgentRunnerRegistry {
    pub protocol_registry: RunnerProtocolRegistry,
    pub workflow_registry: N243WorkflowRegistry,
}

impl AgentRunnerRegistry {
    pub fn new() -> Self {
        Self {
            protocol_registry: RunnerProtocolRegistry::new(),
            workflow_registry: N243WorkflowRegistry::new(),
        }
    }

    /// Validate a runner through the existing L5/L6 protocol.
    pub fn validate_runner(&mut self, target: AgentRunnerId) -> RunnerProtocolResult {
        let change = crate::gates::runner_protocol::RunnerChange::new(
            format!("agent-runner-{}", target.as_str()),
            format!("Validate runner {:?}", target),
        );
        let runner_type = match target {
            AgentRunnerId::Llux => RunnerType::LLUX,
            AgentRunnerId::Timx => RunnerType::TIMX,
            AgentRunnerId::Rootx => RunnerType::ROOTX,
            AgentRunnerId::Tlm => RunnerType::TLMCore,
            AgentRunnerId::Rlm243 => RunnerType::RLM243,
        };
        self.protocol_registry
            .validate_runner(runner_type, &change)
            .expect("runner validation should pass in runner_protocol tests")
    }

    /// Register a workflow bound to the runner registry.
    pub fn register_workflow(&mut self, workflow: N243Workflow) {
        self.workflow_registry.register(workflow);
    }

    /// List workflows for a given event kind.
    pub fn workflows_for_event(&self, event_kind: u64) -> Vec<&N243Workflow> {
        self.workflow_registry.find_by_event_kind(event_kind)
    }
}

impl Default for AgentRunnerRegistry {
    fn default() -> Self {
        Self::new()
    }
}
