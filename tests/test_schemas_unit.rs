// N243 — external unit tests for `src/schemas.rs`
// Coverage: schema validation edge cases not covered by inline tests.

use n243::schemas::{BridgeContractSchema, GovernanceSchema, N243AgentSchema, N243_SCHEMA_VERSION};

#[test]
fn test_agent_schema_version_mismatch_produces_warning() {
    let schema = N243AgentSchema {
        version: "0.0.0".to_string(),
        id: "agent-1".to_string(),
        name: "Test".to_string(),
        stratum: "L4".to_string(),
        capabilities: vec![],
        governance: GovernanceSchema {
            requires_l5_gate: false,
            requires_l6_proof: false,
            allowed_strata: vec![],
            intent_hash_required: false,
        },
    };
    let result = schema.validate();
    assert!(result.valid);
    assert_eq!(result.warnings.len(), 1);
    assert!(result.warnings[0].contains("Schema version mismatch"));
}

#[test]
fn test_agent_schema_empty_id_is_invalid() {
    let schema = N243AgentSchema {
        version: N243_SCHEMA_VERSION.to_string(),
        id: "".to_string(),
        name: "Test".to_string(),
        stratum: "L4".to_string(),
        capabilities: vec![],
        governance: GovernanceSchema {
            requires_l5_gate: false,
            requires_l6_proof: false,
            allowed_strata: vec![],
            intent_hash_required: false,
        },
    };
    let result = schema.validate();
    assert!(!result.valid);
    assert!(result.errors.iter().any(|e| e.contains("Agent ID cannot be empty")));
}

#[test]
fn test_agent_schema_empty_stratum_is_invalid() {
    let schema = N243AgentSchema {
        version: N243_SCHEMA_VERSION.to_string(),
        id: "agent-1".to_string(),
        name: "Test".to_string(),
        stratum: "".to_string(),
        capabilities: vec![],
        governance: GovernanceSchema {
            requires_l5_gate: false,
            requires_l6_proof: false,
            allowed_strata: vec![],
            intent_hash_required: false,
        },
    };
    let result = schema.validate();
    assert!(!result.valid);
    assert!(result.errors.iter().any(|e| e.contains("Stratum cannot be empty")));
}

#[test]
fn test_bridge_contract_empty_source_repo_is_invalid() {
    let contract = BridgeContractSchema {
        source_repo: "".to_string(),
        target_repo: "WAZAA".to_string(),
        protocol: "bus".to_string(),
        version: "1.0".to_string(),
        endpoints: vec!["relay".to_string()],
    };
    let result = contract.validate();
    assert!(!result.valid);
    assert!(result.errors.iter().any(|e| e.contains("Source repo cannot be empty")));
}

#[test]
fn test_bridge_contract_empty_endpoints_is_invalid() {
    let contract = BridgeContractSchema {
        source_repo: "WAZAA".to_string(),
        target_repo: "N243".to_string(),
        protocol: "bus".to_string(),
        version: "1.0".to_string(),
        endpoints: vec![],
    };
    let result = contract.validate();
    assert!(!result.valid);
    assert!(result.errors.iter().any(|e| e.contains("At least one endpoint is required")));
}
