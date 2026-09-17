// N243 — BDCP Enforcer Unit Tests
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use n243::bdcp::enforcer::BdcpEnforcer;
use std::path::Path;

#[test]
fn test_bdcp_enforcer_creation() {
    let enforcer = BdcpEnforcer::new();
    assert!(enforcer.is_stratum_enforced("L4"));
    assert!(!enforcer.is_stratum_enforced("L9"));
}

#[test]
fn test_bdcp_enforcer_default() {
    let enforcer = BdcpEnforcer::default();
    assert!(enforcer.is_stratum_enforced("L4"));
}

#[test]
fn test_bdcp_enforcer_enforce_clone_known_repo() {
    let enforcer = BdcpEnforcer::new();
    let target = Path::new("D:/DO/WEB/TOOLS/L4-TOOLS/WAZAA_TEST");
    let result = enforcer.enforce_clone("WAZAA", target);
    assert!(result.is_ok());
}

#[test]
fn test_bdcp_enforcer_enforce_clone_unknown_repo() {
    let enforcer = BdcpEnforcer::new();
    let target = Path::new("D:/DO/WEB/TOOLS/L4-TOOLS/UNKNOWN");
    let result = enforcer.enforce_clone("UNKNOWN", target);
    assert!(result.is_err());
}

#[test]
fn test_bdcp_enforcer_enforce_clone_existing_path() {
    let enforcer = BdcpEnforcer::new();
    let target = Path::new("D:/DO/WEB/TOOLS/L4-TOOLS/N243");
    let result = enforcer.enforce_clone("N243", target);
    assert!(result.is_err());
}
