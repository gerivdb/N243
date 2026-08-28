// N243 — Memory Gate (Gate Mémoire Ternaire)
// 
// Valide les opérations mémoire (create/update/delete/link) selon la politique ternaire:
// APPROUVER / SUSPENDRE / REJETER
// 
// IntentHash: 0xN243_MEMORY_GATE_20260828
// Version: 1.0.0
// Author: gerivdb
// Date: 2026-08-28

use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::hash::Hash;
use std::time::Duration;
use uuid::Uuid;

/// Décision ternaire N243
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize, Hash)]
pub enum TernaryDecision {
    Approuver,
    Suspendre,
    Rejeter,
}

impl TernaryDecision {
    pub fn as_str(&self) -> &'static str {
        match self {
            TernaryDecision::Approuver => "APPROUVER",
            TernaryDecision::Suspendre => "SUSPENDRE",
            TernaryDecision::Rejeter => "REJETER",
        }
    }
}

/// Type d'opération mémoire
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize, Hash)]
pub enum MemoryOperation {
    Create,
    Update,
    Delete,
    Link,
}

/// Tier de mémoire (AMU)
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize, Hash)]
pub enum MemoryTier {
    Hot,
    Warm,
    Cold,
    Permanent,
}

/// Provenance de l'écriture
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize, Hash)]
pub enum Provenance {
    Brain,
    HermesNr,
    N243,
    Ctulu,
    Human,
    Mnemo,
    KgL,
    Wazaa,
}

/// Domaine mémoire
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize, Hash)]
pub enum MemoryDomain {
    Identity,
    Facts,
    Skills,
    Causal,
    Spectral,
    Decisions,
}

/// Requête de gate mémoire
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MemoryGateRequest {
    pub operation: MemoryOperation,
    pub domain: MemoryDomain,
    pub tier: MemoryTier,
    pub provenance: Provenance,
    pub key: String,
    pub value_hash: Option<String>,
    pub requester: String,
    pub timestamp: String,
}

/// Décision du gate mémoire
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MemoryGateDecision {
    pub decision: TernaryDecision,
    pub reason: String,
    pub request_id: String,
    pub conditions: Vec<String>,
    pub metadata: Option<serde_json::Value>,
}

/// Gate Mémoire N243
pub struct MemoryGate {
    decision_cache: std::sync::RwLock<std::collections::HashMap<String, (TernaryDecision, std::time::Instant)>>,
    policies: HashMap<(MemoryDomain, MemoryTier), GatePolicy>,
    cache_ttl: Duration,
}

#[derive(Debug, Clone)]
struct GatePolicy {
    default_decision: TernaryDecision,
    require_schema_validation: bool,
    require_ttl_for_hot: bool,
    max_value_size_bytes: usize,
    allowed_provenances: Vec<Provenance>,
}

impl MemoryGate {
    pub fn new() -> Self {
        let mut policies = HashMap::new();
        
        policies.insert(
            (MemoryDomain::Identity, MemoryTier::Hot),
            GatePolicy {
                default_decision: TernaryDecision::Approuver,
                require_schema_validation: true,
                require_ttl_for_hot: true,
                max_value_size_bytes: 1024 * 1024,
                allowed_provenances: vec![Provenance::Human, Provenance::Brain, Provenance::HermesNr],
            },
        );
        policies.insert(
            (MemoryDomain::Facts, MemoryTier::Hot),
            GatePolicy {
                default_decision: TernaryDecision::Approuver,
                require_schema_validation: true,
                require_ttl_for_hot: true,
                max_value_size_bytes: 512 * 1024,
                allowed_provenances: vec![Provenance::Human, Provenance::Brain, Provenance::HermesNr, Provenance::N243],
            },
        );
        policies.insert(
            (MemoryDomain::Causal, MemoryTier::Cold),
            GatePolicy {
                default_decision: TernaryDecision::Suspendre,
                require_schema_validation: true,
                require_ttl_for_hot: false,
                max_value_size_bytes: 10 * 1024 * 1024,
                allowed_provenances: vec![Provenance::KgL, Provenance::Ctulu, Provenance::N243],
            },
        );
        
        Self {
            decision_cache: std::sync::RwLock::new(std::collections::HashMap::new()),
            policies,
            cache_ttl: Duration::from_secs(3600),
        }
    }

    fn check_cache(&self, cache_key: &str, request_id: &str) -> Option<MemoryGateDecision> {
        if let Ok(cache) = self.decision_cache.read() {
            if let Some((cached_decision, cached_time)) = cache.get(cache_key) {
                if cached_time.elapsed() < self.cache_ttl {
                    return Some(MemoryGateDecision {
                        decision: *cached_decision,
                        reason: "Cached decision".to_string(),
                        request_id: request_id.to_string(),
                        conditions: vec!["cached".to_string()],
                        metadata: None,
                    });
                }
            }
            None
        } else {
            None
        }
    }

    fn get_policy(&self, domain: MemoryDomain, tier: MemoryTier) -> GatePolicy {
        self.policies.get(&(domain, tier))
            .cloned()
            .unwrap_or_else(|| GatePolicy {
                default_decision: TernaryDecision::Suspendre,
                require_schema_validation: true,
                require_ttl_for_hot: false,
                max_value_size_bytes: 1024 * 1024,
                allowed_provenances: vec![],
            })
    }

    fn check_provenance(&self, policy: &GatePolicy, provenance: Provenance, domain: MemoryDomain) -> (TernaryDecision, String, Vec<String>) {
        let mut conditions = Vec::new();
        let mut decision = policy.default_decision;
        let mut reason = String::new();
        
        if !policy.allowed_provenances.is_empty() && !policy.allowed_provenances.contains(&provenance) {
            decision = TernaryDecision::Rejeter;
            reason = format!("Provenance {:?} non autorisée pour domaine {:?}", provenance, domain);
        } else {
            conditions.push("provenance_valid".to_string());
        }
        (decision, reason, conditions)
    }

    fn check_ttl(&self, policy: &GatePolicy, tier: MemoryTier, conditions: &mut Vec<String>) {
        if policy.require_ttl_for_hot && matches!(tier, MemoryTier::Hot) {
            conditions.push("ttl_required".to_string());
        }
    }

    pub fn validate(&self, request: MemoryGateRequest) -> MemoryGateDecision {
        let request_id = Uuid::new_v4().to_string();
        
        let cache_key = format!("{}:{}:{}:{}", 
            request.operation as u8, 
            request.domain as u8, 
            request.tier as u8, 
            request.key
        );
        
        if let Some(cached) = self.check_cache(&cache_key, &request_id) {
            return cached;
        }
        
        let policy = self.get_policy(request.domain, request.tier);
        
        let mut conditions = Vec::new();
        let mut decision = policy.default_decision;
        
        let (dec, reason, mut conds) = self.check_provenance(&policy, request.provenance, request.domain);
        decision = dec;
        conditions.append(&mut conds);
        
        if policy.require_ttl_for_hot && matches!(request.tier, MemoryTier::Hot) {
            conditions.push("ttl_required".to_string());
        }
        
        if let Ok(mut cache) = self.decision_cache.write() {
            cache.insert(cache_key, (decision, std::time::Instant::now()));
        }
        
        MemoryGateDecision {
            decision,
            reason,
            request_id,
            conditions,
            metadata: None,
        }
    }
    
    pub fn invalidate_cache(&self, key: &str) {
        if let Ok(mut cache) = self.decision_cache.write() {
            cache.retain(|k, _| !k.ends_with(&format!(":{}", key)));
        }
    }
}

impl Default for MemoryGate {
    fn default() -> Self {
        Self::new()
    }
}

pub async fn handle_memory_gate_request(request: serde_json::Value) -> serde_json::Value {
    let gate = MemoryGate::new();
    
    let request: MemoryGateRequest = match serde_json::from_value(request) {
        Ok(r) => r,
        Err(e) => {
            return serde_json::json!({
                "decision": "REJETER",
                "reason": format!("Invalid request: {}", e),
                "request_id": Uuid::new_v4().to_string(),
            });
        }
    };
    
    let decision = gate.validate(request);
    serde_json::to_value(decision).unwrap_or_else(|_| serde_json::json!({
        "decision": "REJETER",
        "reason": "Serialization failed",
        "request_id": Uuid::new_v4().to_string(),
    }))
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_gate_approves_hot_identity() {
        let gate = MemoryGate::new();
        let request = MemoryGateRequest {
            operation: MemoryOperation::Create,
            domain: MemoryDomain::Identity,
            tier: MemoryTier::Hot,
            provenance: Provenance::Human,
            key: "identity:user".to_string(),
            value_hash: None,
            requester: "test-session".to_string(),
            timestamp: chrono::Utc::now().to_rfc3339(),
        };
        
        let decision = gate.validate(request);
        assert_eq!(decision.decision, TernaryDecision::Approuver);
    }
    
    #[test]
    fn test_gate_suspends_cold_causal() {
        let gate = MemoryGate::new();
        let request = MemoryGateRequest {
            operation: MemoryOperation::Create,
            domain: MemoryDomain::Causal,
            tier: MemoryTier::Cold,
            provenance: Provenance::KgL,
            key: "causal:test".to_string(),
            value_hash: None,
            requester: "test-session".to_string(),
            timestamp: chrono::Utc::now().to_rfc3339(),
        };
        
        let decision = gate.validate(request);
        assert_eq!(decision.decision, TernaryDecision::Suspendre);
    }
    
    #[test]
    fn test_gate_rejects_unauthorized_provenance() {
        let gate = MemoryGate::new();
        let request = MemoryGateRequest {
            operation: MemoryOperation::Create,
            domain: MemoryDomain::Identity,
            tier: MemoryTier::Hot,
            provenance: Provenance::Mnemo,
            key: "identity:test".to_string(),
            value_hash: None,
            requester: "test-session".to_string(),
            timestamp: chrono::Utc::now().to_rfc3339(),
        };
        
        let decision = gate.validate(request);
        assert_eq!(decision.decision, TernaryDecision::Rejeter);
    }
}