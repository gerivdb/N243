// N243 — external unit tests for `src/gates/l6.rs`
// Coverage: IntentHash determinism, keypair nonce variance, bad signature bytes,
// verification result construction, proof agent_id preservation.

use n243::gates::l6::{IntentHash, L6KeyPair, L6Proof, L6VerificationResult};
use uuid::Uuid;

#[test]
fn test_l6_intent_hash_is_deterministic() {
    let a = IntentHash::current();
    let b = IntentHash::current();
    assert_eq!(a.0, b.0);
}

#[test]
fn test_l6_key_pair_different_nonces_produce_different_keys() {
    let kp1 = L6KeyPair::generate_with_nonce(1);
    let kp2 = L6KeyPair::generate_with_nonce(2);
    assert_ne!(kp1.signing_key.to_bytes(), kp2.signing_key.to_bytes());
    assert_ne!(
        kp1.verifying_key.to_bytes(),
        kp2.verifying_key.to_bytes()
    );
}

#[test]
fn test_l6_proof_verify_rejects_bad_signature_bytes() {
    let keypair = L6KeyPair::generate();
    let agent_id = Uuid::new_v4();
    let result = serde_json::json!({"status": "success"});

    let mut proof = L6Proof::generate(agent_id, result, &keypair.signing_key);
    proof.signature = vec![0u8; 64];

    assert!(!proof.verify(&keypair.verifying_key));
}

#[test]
fn test_l6_verification_result_can_be_constructed() {
    let proof = L6Proof::generate(
        Uuid::new_v4(),
        serde_json::json!({}),
        &L6KeyPair::generate().signing_key,
    );
    let result = L6VerificationResult {
        passed: true,
        proof: Some(proof),
        error: None,
    };
    assert!(result.passed);
    assert!(result.proof.is_some());
    assert!(result.error.is_none());
}

#[test]
fn test_l6_proof_preserves_same_agent_id() {
    let keypair = L6KeyPair::generate();
    let agent_id = Uuid::new_v4();
    let result = serde_json::json!({"status": "success"});

    let proof = L6Proof::generate(agent_id, result, &keypair.signing_key);
    assert_eq!(proof.agent_id, agent_id);
}
