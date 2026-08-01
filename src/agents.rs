// N243 — Agents
// Cognitive agent definitions for the N243 meta-orchestrator.

use serde::{Deserialize, Serialize};
use std::collections::HashMap;

/// Agent identifier
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq, Hash)]
pub struct AgentId(pub String);

/// Agent status
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub enum AgentStatus {
    Idle,
    Running,
    Completed,
    Failed,
}

/// Cognitive agent in the N243 orchestrator
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Agent {
    pub id: AgentId,
    pub name: String,
    pub status: AgentStatus,
    pub capabilities: Vec<String>,
    pub current_task: Option<String>,
    pub metadata: HashMap<String, String>,
}

impl Agent {
    pub fn new(id: impl Into<String>, name: impl Into<String>) -> Self {
        Self {
            id: AgentId(id.into()),
            name: name.into(),
            status: AgentStatus::Idle,
            capabilities: Vec::new(),
            current_task: None,
            metadata: HashMap::new(),
        }
    }

    pub fn with_capabilities(mut self, capabilities: Vec<String>) -> Self {
        self.capabilities = capabilities;
        self
    }

    pub fn assign_task(&mut self, task: impl Into<String>) {
        self.current_task = Some(task.into());
        self.status = AgentStatus::Running;
    }

    pub fn complete(&mut self) {
        self.status = AgentStatus::Completed;
        self.current_task = None;
    }

    pub fn fail(&mut self, reason: impl Into<String>) {
        self.status = AgentStatus::Failed;
        self.metadata.insert("failure_reason".to_string(), reason.into());
    }
}

/// Agent registry for N243
#[derive(Debug, Clone, Default)]
pub struct AgentRegistry {
    agents: HashMap<AgentId, Agent>,
}

impl AgentRegistry {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn register(&mut self, agent: Agent) {
        self.agents.insert(agent.id.clone(), agent);
    }

    pub fn get(&self, id: &AgentId) -> Option<&Agent> {
        self.agents.get(id)
    }

    pub fn get_mut(&mut self, id: &AgentId) -> Option<&mut Agent> {
        self.agents.get_mut(id)
    }

    pub fn list_idle(&self) -> Vec<&Agent> {
        self.agents
            .values()
            .filter(|a| a.status == AgentStatus::Idle)
            .collect()
    }

    pub fn list_running(&self) -> Vec<&Agent> {
        self.agents
            .values()
            .filter(|a| a.status == AgentStatus::Running)
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_agent_lifecycle() {
        let mut agent = Agent::new("agent-1", "TestAgent");
        assert_eq!(agent.status, AgentStatus::Idle);

        agent.assign_task("process-event-7");
        assert_eq!(agent.status, AgentStatus::Running);
        assert_eq!(agent.current_task, Some("process-event-7".to_string()));

        agent.complete();
        assert_eq!(agent.status, AgentStatus::Completed);
        assert!(agent.current_task.is_none());
    }

    #[test]
    fn test_agent_registry() {
        let mut registry = AgentRegistry::new();
        let agent = Agent::new("a1", "Alpha").with_capabilities(vec!["relay".to_string()]);
        registry.register(agent);

        assert!(registry.get(&AgentId("a1".to_string())).is_some());
        assert_eq!(registry.list_idle().len(), 1);
    }
}
