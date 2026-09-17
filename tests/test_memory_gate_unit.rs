// N243 — external unit tests for `src/gates/memory_gate.rs`
// Coverage: cache reuse, invalidate_cache behavior, same-key fresh decision,
// unauthorized provenance rejection, valid hot/identity approval.

use n243::gates::memory_gate::{
    MemoryDomain, MemoryGate, MemoryOperation, MemoryTier, Provenance, TernaryDecision,
};

#[test]
fn test_memory_gate_cache_hit_returns_cached_decision() {
    let gate = MemoryGate::new();
    let request = |key: &str| n243::gates::memory_gate::MemoryGateRequest {
        operation: MemoryOperation::Create,
        domain: MemoryDomain::Identity,
        tier: MemoryTier::Hot,
        provenance: Provenance::Human,
        key: key.to_string(),
        value_hash: None,
        requester: "test".to_string(),
        timestamp: chrono::Utc::now().to_rfc3339(),
    };

    let first = gate.validate(request("cache-key"));
    let second = gate.validate(request("cache-key"));

    assert_eq!(first.decision, second.decision);
    assert_eq!(second.reason, "Cached decision");
    assert!(second.conditions.contains(&"cached".to_string()));
}

#[test]
fn test_memory_gate_different_keys_are_independent() {
    let gate = MemoryGate::new();
    let request = |key: &str| n243::gates::memory_gate::MemoryGateRequest {
        operation: MemoryOperation::Create,
        domain: MemoryDomain::Identity,
        tier: MemoryTier::Hot,
        provenance: Provenance::Human,
        key: key.to_string(),
        value_hash: None,
        requester: "test".to_string(),
        timestamp: chrono::Utc::now().to_rfc3339(),
    };

    let first = gate.validate(request("key-a"));
    let second = gate.validate(request("key-b"));

    assert_ne!(first.request_id, second.request_id);
    assert_eq!(first.decision, TernaryDecision::Approuver);
    assert_eq!(second.decision, TernaryDecision::Approuver);
}

#[test]
fn test_memory_gate_invalidate_cache_removes_matching_key() {
    let gate = MemoryGate::new();
    let request = |key: &str| n243::gates::memory_gate::MemoryGateRequest {
        operation: MemoryOperation::Create,
        domain: MemoryDomain::Identity,
        tier: MemoryTier::Hot,
        provenance: Provenance::Human,
        key: key.to_string(),
        value_hash: None,
        requester: "test".to_string(),
        timestamp: chrono::Utc::now().to_rfc3339(),
    };

    let first = gate.validate(request("evict-key"));
    gate.invalidate_cache("evict-key");
    let second = gate.validate(request("evict-key"));

    assert_ne!(first.request_id, second.request_id);
}

#[test]
fn test_memory_gate_unauthorized_provance_is_rejected() {
    let gate = MemoryGate::new();
    let request = n243::gates::memory_gate::MemoryGateRequest {
        operation: MemoryOperation::Create,
        domain: MemoryDomain::Identity,
        tier: MemoryTier::Hot,
        provenance: Provenance::Mnemo,
        key: "identity:test".to_string(),
        value_hash: None,
        requester: "test".to_string(),
        timestamp: chrono::Utc::now().to_rfc3339(),
    };

    let decision = gate.validate(request);
    assert_eq!(decision.decision, TernaryDecision::Rejeter);
}

#[test]
fn test_memory_gate_valid_hot_identity_is_approved() {
    let gate = MemoryGate::new();
    let request = n243::gates::memory_gate::MemoryGateRequest {
        operation: MemoryOperation::Create,
        domain: MemoryDomain::Identity,
        tier: MemoryTier::Hot,
        provenance: Provenance::Human,
        key: "identity:user".to_string(),
        value_hash: None,
        requester: "test".to_string(),
        timestamp: chrono::Utc::now().to_rfc3339(),
    };

    let decision = gate.validate(request);
    assert_eq!(decision.decision, TernaryDecision::Approuver);
    assert!(decision.conditions.contains(&"provenance_valid".to_string()));
}
