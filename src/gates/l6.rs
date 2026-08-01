// N243/gates/l6.rs
// L6 Proof — Preuve d'exécution avec signature Ed25519
// IntentHash: 0xN243_L6_PROOF_20260801

use ed25519_dalek::{SigningKey, Signature, Signer, VerifyingKey, Verifier};
use serde::{Deserialize, Serialize};
use uuid::Uuid;
use chrono::{DateTime, Utc};

/// Hash d'intention pour la traçabilité
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub struct IntentHash(pub [u8; 32]);

impl IntentHash {
    pub fn current() -> Self {
        let mut bytes = [0u8; 32];
        bytes[0..16].copy_from_slice(b"XFORGE_SUITE_2026");
        IntentHash(bytes)
    }
}

/// Preuve L6 — Exécution vérifiable et signée
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct L6Proof {
    pub intent_hash: IntentHash,
    pub timestamp: DateTime<Utc>,
    pub agent_id: Uuid,
    pub result: serde_json::Value,
    pub signature: Vec<u8>,  // Ed25519 signature
}

impl L6Proof {
    /// Génère une preuve L6 signée
    pub fn generate(
        agent_id: Uuid,
        result: serde_json::Value,
        private_key: &SigningKey,
    ) -> Self {
        let intent_hash = IntentHash::current();
        let timestamp = Utc::now();

        let result_bytes = serde_json::to_vec(&result).unwrap_or_default();
        let mut message = Vec::new();
        message.extend_from_slice(&intent_hash.0);
        message.extend_from_slice(&timestamp.timestamp().to_le_bytes());
        message.extend_from_slice(agent_id.as_bytes());
        message.extend_from_slice(&result_bytes);

        let signature: Signature = private_key.sign(&message);

        L6Proof {
            intent_hash,
            timestamp,
            agent_id,
            result,
            signature: signature.to_bytes().to_vec(),
        }
    }

    /// Vérifie la signature de la preuve
    pub fn verify(&self, public_key: &VerifyingKey) -> bool {
        let result_bytes = serde_json::to_vec(&self.result).unwrap_or_default();
        let mut message = Vec::new();
        message.extend_from_slice(&self.intent_hash.0);
        message.extend_from_slice(&self.timestamp.timestamp().to_le_bytes());
        message.extend_from_slice(self.agent_id.as_bytes());
        message.extend_from_slice(&result_bytes);

        let Ok(signature) = Signature::from_slice(&self.signature) else {
            return false;
        };

        public_key.verify(&message, &signature).is_ok()
    }
}

/// Résultat de vérification L6
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct L6VerificationResult {
    pub passed: bool,
    pub proof: Option<L6Proof>,
    pub error: Option<String>,
}

/// Générateur de clés pour L6
pub struct L6KeyPair {
    pub signing_key: SigningKey,
    pub verifying_key: VerifyingKey,
}

impl L6KeyPair {
    pub fn generate() -> Self {
        // TODO: use a CSPRNG when rand/rand_core conflicts are resolved.
        let mut seed = [0u8; 32];
        seed[..16].copy_from_slice(b"N243_L6_KEY_SEED_2026");
        let signing_key = SigningKey::from_bytes(&seed);
        let verifying_key = signing_key.verifying_key();
        Self { signing_key, verifying_key }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_l6_proof_generation_and_verification() {
        let keypair = L6KeyPair::generate();
        let agent_id = Uuid::new_v4();
        let result = serde_json::json!({"status": "success", "output": "test"});

        let proof = L6Proof::generate(agent_id, result.clone(), &keypair.signing_key);
        
        assert_eq!(proof.agent_id, agent_id);
        assert_eq!(proof.result, result);
        assert!(proof.verify(&keypair.verifying_key));
    }

    #[test]
    fn test_l6_proof_fails_with_wrong_key() {
        let keypair1 = L6KeyPair::generate();
        let keypair2 = L6KeyPair::generate();
        let agent_id = Uuid::new_v4();
        let result = serde_json::json!({"status": "success"});

        let proof = L6Proof::generate(agent_id, result, &keypair1.signing_key);
        
        assert!(!proof.verify(&keypair2.verifying_key));
    }
}