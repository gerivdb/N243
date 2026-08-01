// N243 — Schemas
// Schema definitions for N243 governance and cross-repo contracts.

use serde::{Deserialize, Serialize};

/// N243 governance schema version
pub const N243_SCHEMA_VERSION: &str = "1.0.0";

/// Core schema for N243 agent configuration
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct N243AgentSchema {
    pub version: String,
    pub id: String,
    pub name: String,
    pub stratum: String,
    pub capabilities: Vec<String>,
    pub governance: GovernanceSchema,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GovernanceSchema {
    pub requires_l5_gate: bool,
    pub requires_l6_proof: bool,
    pub allowed_strata: Vec<String>,
    pub intent_hash_required: bool,
}

/// Schema for cross-repo bridge contracts
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BridgeContractSchema {
    pub source_repo: String,
    pub target_repo: String,
    pub protocol: String,
    pub version: String,
    pub endpoints: Vec<String>,
}

/// Schema validation result
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SchemaValidationResult {
    pub valid: bool,
    pub errors: Vec<String>,
    pub warnings: Vec<String>,
}

impl N243AgentSchema {
    pub fn validate(&self) -> SchemaValidationResult {
        let mut errors = Vec::new();
        let mut warnings = Vec::new();

        if self.version != N243_SCHEMA_VERSION {
            warnings.push(format!(
                "Schema version mismatch: expected {}, got {}",
                N243_SCHEMA_VERSION, self.version
            ));
        }

        if self.id.is_empty() {
            errors.push("Agent ID cannot be empty".to_string());
        }

        if self.stratum.is_empty() {
            errors.push("Stratum cannot be empty".to_string());
        }

        SchemaValidationResult {
            valid: errors.is_empty(),
            errors,
            warnings,
        }
    }
}

impl BridgeContractSchema {
    pub fn validate(&self) -> SchemaValidationResult {
        let mut errors = Vec::new();

        if self.source_repo.is_empty() {
            errors.push("Source repo cannot be empty".to_string());
        }
        if self.target_repo.is_empty() {
            errors.push("Target repo cannot be empty".to_string());
        }
        if self.endpoints.is_empty() {
            errors.push("At least one endpoint is required".to_string());
        }

        SchemaValidationResult {
            valid: errors.is_empty(),
            errors,
            warnings: Vec::new(),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_agent_schema_validation() {
        let schema = N243AgentSchema {
            version: N243_SCHEMA_VERSION.to_string(),
            id: "agent-1".to_string(),
            name: "Test".to_string(),
            stratum: "L4".to_string(),
            capabilities: vec!["relay".to_string()],
            governance: GovernanceSchema {
                requires_l5_gate: true,
                requires_l6_proof: false,
                allowed_strata: vec!["L4".to_string()],
                intent_hash_required: true,
            },
        };
        let result = schema.validate();
        assert!(result.valid);
    }

    #[test]
    fn test_bridge_contract_validation() {
        let contract = BridgeContractSchema {
            source_repo: "WAZAA".to_string(),
            target_repo: "BUZZ-X".to_string(),
            protocol: "buzz-bridge".to_string(),
            version: "1.0".to_string(),
            endpoints: vec!["relay".to_string(), "acp".to_string()],
        };
        let result = contract.validate();
        assert!(result.valid);
    }
}
