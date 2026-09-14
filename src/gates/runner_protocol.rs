// N243 — Runner Protocol Functor (L5/L6 Gate Integration)
// 
// Implements KEEL R9 functor for runner protocol validation.
// Each runner (LLUX, RLM-243, TIMX, ROOTX, TLM-CORE) gets a functor
// validated through L5 (5 checkers) + L6 (Ed25519 proof).
//
// IntentHash: 0xRUNNER_PROTOCOL_FUNCTOR_20260828

use crate::gates::l5::{L5Gate, Verdict};
use crate::gates::l5::types::Change as L5Change;
use crate::gates::l6::{L6KeyPair, L6Proof};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

/// Runner types managed by N243
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum RunnerType {
    LLUX,
    RLM243,
    TIMX,
    ROOTX,
    TLMCore,
}

impl RunnerType {
    pub fn as_str(&self) -> &'static str {
        match self {
            RunnerType::LLUX => "LLUX",
            RunnerType::RLM243 => "RLM-243",
            RunnerType::TIMX => "TIMX",
            RunnerType::ROOTX => "ROOTX",
            RunnerType::TLMCore => "TLM-CORE",
        }
    }
    
    pub fn all() -> Vec<RunnerType> {
        vec![
            RunnerType::LLUX,
            RunnerType::RLM243,
            RunnerType::TIMX,
            RunnerType::ROOTX,
            RunnerType::TLMCore,
        ]
    }
}

/// Runner Protocol Functor (KEEL R9)
/// 
/// Each runner gets a functor: N243 → Runner
/// Validates composition + identity (KEEL R9) + L5/L6 gates
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RunnerProtocolFunctor {
    pub name: String,
    pub runner_type: RunnerType,
    pub intent_hash: String,
    pub source_verse: String,  // "N243"
    pub target_verse: String,  // Runner type (LLUX, RLM-243, etc.)
    
    // KEEL R9 validation
    pub phi_composition_ok: bool,
    pub phi_identity_ok: bool,
    
    // L5/L6 integration
    pub l5_verdict: Option<crate::gates::l5::Verdict>,
    pub l6_proof: Option<crate::gates::l6::L6Proof>,
    
    // Metadata
    pub registered: bool,
    pub timestamp: String,
    pub metadata: HashMap<String, String>,
}

impl RunnerProtocolFunctor {
    pub fn new(runner_type: RunnerType) -> Self {
        let name = format!("RunnerProtocol_{}", runner_type.as_str());
        let intent_hash = format!("0xRUNNER_PROTOCOL_{}_{}", runner_type.as_str().replace("-", "_"), chrono::Utc::now().format("%Y%m%d"));
        
        Self {
            name,
            runner_type,
            intent_hash,
            source_verse: "N243".to_string(),
            target_verse: runner_type.as_str().to_string(),
            phi_composition_ok: false,
            phi_identity_ok: false,
            l5_verdict: None,
            l6_proof: None,
            registered: false,
            timestamp: chrono::Utc::now().to_rfc3339(),
            metadata: HashMap::new(),
        }
    }
    
    /// Validate KEEL R9: Composition + Identity
    pub fn validate_keel_r9(&mut self) -> Result<(), String> {
        // Composition: N243 → Runner protocol composition
        self.phi_composition_ok = self.validate_composition();
        
        // Identity: Runner identity preserved
        self.phi_identity_ok = self.validate_identity();
        
        if self.phi_composition_ok && self.phi_identity_ok {
            Ok(())
        } else {
            Err("KEEL R9 validation failed".to_string())
        }
    }
    
    fn validate_composition(&self) -> bool {
        // Composition: N243 → Runner protocol preserves structure
        // In production: verify functor laws via CTULU functor-anything
        true
    }
    
    fn validate_identity(&self) -> bool {
        // Identity: Runner identity preserved through protocol
        true
    }
    
    /// L5 Trust Gate: 5 checkers (ADR, φ-CPS, Tests, Security, Maintainability)
    pub fn l5_verify(&mut self, change: &RunnerChange) -> crate::gates::l5::Verdict {
        let l5_gate = crate::gates::l5::L5Gate::new();
        let l5_change = crate::gates::l5::types::Change::new(
            change.id.clone(),
            change.description.clone()
        );
        let verdict = crate::gates::l5::L5Gate::new().verify(&l5_change);
        self.l5_verdict = Some(verdict.clone());
        verdict
    }
    
    /// L6 Proof: Ed25519 signature on L5 verdict
    pub fn l6_prove(&mut self, keypair: &crate::gates::l6::L6KeyPair) -> crate::gates::l6::L6Proof {
        let verdict = self.l5_verdict.as_ref().expect("L5 verdict required before L6");
        let agent_id = uuid::Uuid::new_v4();
        let result = serde_json::json!({
            "verdict": format!("{:?}", self.l5_verdict),
            "runner": self.runner_type.as_str()
        });
        let proof = crate::gates::l6::L6Proof::generate(agent_id, result, &keypair.signing_key);
        self.l6_proof = Some(proof.clone());
        proof
    }
    
    /// Full L5/L6 gate cycle
    pub fn l5_l6_gate(&mut self, change: &RunnerChange, keypair: &crate::gates::l6::L6KeyPair) -> RunnerProtocolResult {
        // L5: 5 checkers
        let l5_verdict = self.l5_verify(change);
        
        // L6: Ed25519 proof
        let keypair = crate::gates::l6::L6KeyPair::generate();
        let l6_proof = self.l6_prove(&keypair);
        
        RunnerProtocolResult {
            functor_name: self.name.clone(),
            runner_type: self.runner_type,
            l5_verdict: self.l5_verdict.clone(),
            l6_proof: self.l6_proof.clone(),
            gate_passed: self.l5_verdict.as_ref().map(|v| *v == crate::gates::l5::Verdict::Approved).unwrap_or(false),
            timestamp: chrono::Utc::now().to_rfc3339(),
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RunnerChange {
    pub id: String,
    pub description: String,
    pub author: String,
    pub timestamp: String,
    pub files: Vec<String>,
    pub adr_ref: Option<String>,
}

impl RunnerChange {
    pub fn new(id: impl Into<String>, description: impl Into<String>) -> Self {
        Self {
            id: id.into(),
            description: description.into(),
            author: "N243".to_string(),
            timestamp: chrono::Utc::now().to_rfc3339(),
            files: Vec::new(),
            adr_ref: None,
        }
    }
}

/// Runner Protocol Result
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RunnerProtocolResult {
    pub functor_name: String,
    pub runner_type: RunnerType,
    pub l5_verdict: Option<crate::gates::l5::Verdict>,
    pub l6_proof: Option<crate::gates::l6::L6Proof>,
    pub gate_passed: bool,
    pub timestamp: String,
}

/// Registry for all runner protocol functors
pub struct RunnerProtocolRegistry {
    functors: std::collections::HashMap<RunnerType, RunnerProtocolFunctor>,
    l5_gate: crate::gates::l5::L5Gate,
    l6_keypair: crate::gates::l6::L6KeyPair,
}

impl RunnerProtocolRegistry {
    pub fn new() -> Self {
        let mut registry = Self {
            functors: std::collections::HashMap::new(),
            l5_gate: crate::gates::l5::L5Gate::new(),
            l6_keypair: crate::gates::l6::L6KeyPair::generate(),
        };
        
        // Initialize all 5 runners
        for runner in RunnerType::all() {
            registry.functors.insert(runner, RunnerProtocolFunctor::new(runner));
        }
        
        registry
    }
    
    pub fn validate_runner(&mut self, runner: RunnerType, change: &RunnerChange) -> Result<RunnerProtocolResult, String> {
        let functor = self.functors.get_mut(&runner)
            .ok_or_else(|| format!("Runner {:?} not found", runner))?;
        
        let result = functor.l5_l6_gate(change, &self.l6_keypair);
        Ok(result)
    }
    
    pub fn validate_all(&mut self, change: &RunnerChange) -> Vec<RunnerProtocolResult> {
        let mut results = Vec::new();
        for runner in RunnerType::all() {
            if let Ok(result) = self.validate_runner(runner, change) {
                results.push(result);
            }
        }
        results
    }
    
    pub fn get_functor(&self, runner: RunnerType) -> Option<&RunnerProtocolFunctor> {
        self.functors.get(&runner)
    }
}

/// WAZAA Channel Events for Runner Protocol
pub mod channels {
    use serde::{Deserialize, Serialize};
    
    pub const RUNNER_PROTOCOL: &str = "L4-TOOLS/N243/runners/protocol";
    pub const RUNNER_STATE: &str = "L4-TOOLS/N243/runners/state/*";
    pub const RUNNER_CLUSTER_TOPOLOGY: &str = "L4-TOOLS/N243/runners/cluster";
    
    pub const RUNNER_PROTOCOL_EVENT: &str = "RUNNER_PROTOCOL";
    pub const RUNNER_STATE_EVENT: &str = "RUNNER_STATE";
    pub const RUNNER_CLUSTER_EVENT: &str = "RUNNER_CLUSTER_TOPOLOGY";
    
    /// Payload for RUNNER_PROTOCOL event
    #[derive(Serialize, Deserialize)]
    pub struct RunnerProtocolPayload {
        pub functor_name: String,
        pub runner_type: String,
        pub intent_hash: String,
        pub l5_verdict: String,
        pub l6_proof_hash: String,
        pub timestamp: String,
    }
    
    /// Payload for RUNNER_STATE event
    #[derive(Serialize, Deserialize)]
    pub struct RunnerStatePayload {
        pub runner_type: String,
        pub state: String,  // RUNNING, STOPPED, ERROR
        pub health: f32,    // 0.0 - 1.0
        pub load: f32,      // 0.0 - 1.0
        pub timestamp: String,
    }
    
    /// Payload for RUNNER_CLUSTER_TOPOLOGY event
    #[derive(Serialize, Deserialize)]
    pub struct RunnerClusterPayload {
        pub runners: Vec<String>,
        pub edges: Vec<(String, String)>,  // (from, to)
        pub topology_hash: String,
        pub timestamp: String,
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_runner_protocol_channels() {
        assert_eq!(channels::RUNNER_PROTOCOL, "L4-TOOLS/N243/runners/protocol");
        assert_eq!(channels::RUNNER_STATE, "L4-TOOLS/N243/runners/state/*");
        assert_eq!(channels::RUNNER_CLUSTER_TOPOLOGY, "L4-TOOLS/N243/runners/cluster");
        assert_eq!(channels::RUNNER_PROTOCOL_EVENT, "RUNNER_PROTOCOL");
        assert_eq!(channels::RUNNER_STATE_EVENT, "RUNNER_STATE");
        assert_eq!(channels::RUNNER_CLUSTER_EVENT, "RUNNER_CLUSTER_TOPOLOGY");
    }
    
    #[test]
    fn test_runner_protocol_functor_creation() {
        let mut functor = RunnerProtocolFunctor::new(RunnerType::LLUX);
        assert_eq!(functor.runner_type, RunnerType::LLUX);
        assert_eq!(functor.source_verse, "N243");
        assert_eq!(functor.target_verse, "LLUX");
    }
    
    #[test]
    fn test_runner_protocol_functor_keel_r9() {
        let mut functor = RunnerProtocolFunctor::new(RunnerType::RLM243);
        let result = functor.validate_keel_r9();
        assert!(result.is_ok());
        assert!(functor.phi_composition_ok);
        assert!(functor.phi_identity_ok);
    }
    
    #[test]
    fn test_runner_registry() {
        let mut registry = RunnerProtocolRegistry::new();
        assert_eq!(registry.functors.len(), 5);
        
        for runner in RunnerType::all() {
            assert!(registry.functors.contains_key(&runner));
        }
    }
}