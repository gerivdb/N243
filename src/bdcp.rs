// N243 — BDCP Integration
// Enforcement BDCP N243 natif (PRD-005) — pivot WAZAA 2026-08-23 (Buzz@block abandonné).

use std::collections::HashMap;
use std::path::Path;

/// Repo entry for BDCP checking.
#[derive(Debug, Clone)]
pub struct RepoEntry {
    pub name: String,
    pub local_path: String,
    pub stratum: String,
    pub status: String,
    pub upstream: Option<String>,
    pub license: String,
}

/// BDCP checker N243 (PRD-005) — valide contre la SOT connue.
#[derive(Debug, Clone)]
pub struct BDCPChecker {
    pub known_repos: HashMap<String, RepoEntry>,
}

/// BDCP error types.
#[derive(Debug, Clone, thiserror::Error)]
pub enum BDCPError {
    #[error("repo not declared: {0}")]
    RepoNotDeclared(String),
    #[error("repo already exists: {0}")]
    RepoAlreadyExists(String),
    #[error("invalid stratum: {0}")]
    InvalidStratum(String),
}

impl BDCPChecker {
    pub fn check_clone(&self, repo_name: &str, target_path: &Path) -> Result<(), BDCPError> {
        if !self.known_repos.contains_key(repo_name) {
            return Err(BDCPError::RepoNotDeclared(repo_name.to_string()));
        }
        if target_path.exists() {
            return Err(BDCPError::RepoAlreadyExists(repo_name.to_string()));
        }
        let entry = &self.known_repos[repo_name];
        if !entry.local_path.starts_with("D:/DO/WEB/TOOLS/L") {
            return Err(BDCPError::InvalidStratum(entry.stratum.clone()));
        }
        Ok(())
    }
}

/// N243 BDCP governor — applique les règles de clone (strates L*, SOT).
pub struct N243BDCPGovernor {
    checker: BDCPChecker,
    enforced_strata: Vec<&'static str>,
}

impl N243BDCPGovernor {
    pub fn new() -> Self {
        let mut known_repos = HashMap::new();
        known_repos.insert(
            "WAZAA".to_string(),
            RepoEntry {
                name: "WAZAA".to_string(),
                local_path: "D:/DO/WEB/TOOLS/L4-TOOLS/WAZAA".to_string(),
                stratum: "L4".to_string(),
                status: "active".to_string(),
                upstream: Some("https://github.com/gerivdb/WAZAA".to_string()),
                license: "Apache-2.0".to_string(),
            },
        );
        known_repos.insert(
            "N243".to_string(),
            RepoEntry {
                name: "N243".to_string(),
                local_path: "D:/DO/WEB/TOOLS/L4-TOOLS/N243".to_string(),
                stratum: "L4".to_string(),
                status: "active".to_string(),
                upstream: Some("https://github.com/gerivdb/N243".to_string()),
                license: "Apache-2.0".to_string(),
            },
        );

        Self {
            checker: BDCPChecker { known_repos },
            enforced_strata: vec!["L0", "L1", "L2", "L3", "L4", "L5"],
        }
    }

    /// Validate a clone target against BDCP rules.
    pub fn validate_clone(&self, repo_name: &str, target_path: &Path) -> Result<(), BDCPError> {
        self.checker.check_clone(repo_name, target_path)
    }

    /// Check if a stratum is enforced by N243.
    pub fn is_stratum_enforced(&self, stratum: &str) -> bool {
        self.enforced_strata.contains(&stratum)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::path::PathBuf;

    #[test]
    fn test_n243_bdcp_governor_creation() {
        let gov = N243BDCPGovernor::new();
        assert!(gov.is_stratum_enforced("L4"));
        assert!(!gov.is_stratum_enforced("L9"));
    }

    #[test]
    fn test_validate_known_repo() {
        let gov = N243BDCPGovernor::new();
        let target = PathBuf::from("D:/DO/WEB/TOOLS/L4-TOOLS/WAZAA_TEST");
        let result = gov.validate_clone("WAZAA", &target);
        assert!(result.is_ok());
    }

    #[test]
    fn test_reject_unknown_repo() {
        let gov = N243BDCPGovernor::new();
        let target = PathBuf::from("D:/DO/WEB/TOOLS/L4-TOOLS/UNKNOWN");
        let result = gov.validate_clone("UNKNOWN", &target);
        assert!(matches!(result, Err(BDCPError::RepoNotDeclared(_))));
    }
}
