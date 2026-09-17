// N243 — BDCP Enforcer
// Point d'entrée d'exécution des règles BDCP.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use crate::bdcp::{BDCPError, N243BDCPGovernor};
use std::path::Path;

/// BDCP enforcer for N243.
pub struct BdcpEnforcer {
    governor: N243BDCPGovernor,
}

impl BdcpEnforcer {
    /// Create a new enforcer.
    pub fn new() -> Self {
        Self {
            governor: N243BDCPGovernor::new(),
        }
    }

    /// Enforce BDCP rules for a clone operation.
    pub fn enforce_clone(&self, repo_name: &str, target_path: &Path) -> Result<(), BDCPError> {
        self.governor.validate_clone(repo_name, target_path)
    }

    /// Check if a stratum is enforced.
    pub fn is_stratum_enforced(&self, stratum: &str) -> bool {
        self.governor.is_stratum_enforced(stratum)
    }
}

impl Default for BdcpEnforcer {
    fn default() -> Self {
        Self::new()
    }
}
