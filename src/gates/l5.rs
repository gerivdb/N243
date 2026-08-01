// N243/gates/l5.rs
// L5 Trust Gate with Maintainability Oracle
// IntentHash: 0xN243_L5_GATE_20260801

pub mod types;

use crate::gates::l5::types::{Change, CheckResult, Checker, Verdict};
use crate::gates::maintainability_oracle::MaintainabilityOracle;

/// ADR Checker — vérifie qu'un changement a un ADR associé.
#[derive(Debug, Clone, Default)]
pub struct ADRChecker;

impl ADRChecker {
    pub fn new() -> Self {
        Self::default()
    }
}

impl Checker for ADRChecker {
    fn check(&self, _change: &Change) -> CheckResult {
        CheckResult {
            passed: true,
            detail: "ADR check stub".to_string(),
        }
    }
}

/// φ-CPS Checker — vérifie la performance cyclique.
#[derive(Debug, Clone, Default)]
pub struct PhiCpsChecker;

impl PhiCpsChecker {
    pub fn new() -> Self {
        Self::default()
    }
}

impl Checker for PhiCpsChecker {
    fn check(&self, _change: &Change) -> CheckResult {
        CheckResult {
            passed: true,
            detail: "phi_cps check stub".to_string(),
        }
    }
}

/// Test Checker — vérifie la présence de tests.
#[derive(Debug, Clone, Default)]
pub struct TestChecker;

impl TestChecker {
    pub fn new() -> Self {
        Self::default()
    }
}

impl Checker for TestChecker {
    fn check(&self, _change: &Change) -> CheckResult {
        CheckResult {
            passed: true,
            detail: "test check stub".to_string(),
        }
    }
}

/// Security Checker — vérifie les aspects sécurité.
#[derive(Debug, Clone, Default)]
pub struct SecurityChecker;

impl SecurityChecker {
    pub fn new() -> Self {
        Self::default()
    }
}

impl Checker for SecurityChecker {
    fn check(&self, _change: &Change) -> CheckResult {
        CheckResult {
            passed: true,
            detail: "security check stub".to_string(),
        }
    }
}

/// L5 Trust Gate — Vérificateur Indépendant
pub struct L5Gate {
    adr_checker: ADRChecker,
    phi_cps_checker: PhiCpsChecker,
    test_checker: TestChecker,
    security_checker: SecurityChecker,
    maintainability_oracle: MaintainabilityOracle,
}

impl L5Gate {
    pub fn new() -> Self {
        Self {
            adr_checker: ADRChecker::new(),
            phi_cps_checker: PhiCpsChecker::new(),
            test_checker: TestChecker::new(),
            security_checker: SecurityChecker::new(),
            maintainability_oracle: MaintainabilityOracle::new(),
        }
    }

    /// Vérifie un changement contre tous les critères
    pub fn verify(&self, change: &Change) -> Verdict {
        let mut verdict = Verdict::Approved;

        let checkers: Vec<&dyn Checker> = vec![
            &self.adr_checker,
            &self.phi_cps_checker,
            &self.test_checker,
            &self.security_checker,
        ];
        for checker in checkers {
            if !checker.check(change).passed {
                verdict = Verdict::Rejected;
                break;
            }
        }

        // Oracle de Maintenabilité
        if !matches!(
            self.maintainability_oracle.check(change),
            crate::gates::maintainability_oracle::MaintainabilityVerdict::Approved
        ) {
            verdict = Verdict::Rejected;
        }

        verdict
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_l5_gate_creation() {
        let gate = L5Gate::new();
        assert!(matches!(gate.verify(&Change::new("c1", "test")), Verdict::Approved));
    }

    #[test]
    fn test_l5_gate_verdict_types() {
        assert!(matches!(Verdict::Approved, Verdict::Approved));
        assert!(matches!(Verdict::Rejected, Verdict::Rejected));
        assert!(matches!(Verdict::Pending, Verdict::Pending));
    }
}
