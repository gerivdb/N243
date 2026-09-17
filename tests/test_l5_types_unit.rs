// N243 — unit tests for `src/gates/l5/types.rs`
// Coverage: Change construction, Verdict default, Checker trait implementation.

use n243::gates::l5::{Change, CheckResult, Checker, Verdict};

struct AlwaysPassChecker;

impl Checker for AlwaysPassChecker {
    fn check(&self, _change: &Change) -> CheckResult {
        CheckResult {
            passed: true,
            detail: "always pass".to_string(),
        }
    }
}

struct AlwaysFailChecker;

impl Checker for AlwaysFailChecker {
    fn check(&self, _change: &Change) -> CheckResult {
        CheckResult {
            passed: false,
            detail: "always fail".to_string(),
        }
    }
}

#[test]
fn test_change_new_sets_fields() {
    let change = Change::new("c-1", "desc");
    assert_eq!(change.id, "c-1");
    assert_eq!(change.description, "desc");
    assert!(change.files.is_empty());
}

#[test]
fn test_verdict_default_is_approved() {
    let verdict: Verdict = Default::default();
    assert_eq!(verdict, Verdict::Approved);
}

#[test]
fn test_checker_always_pass() {
    let checker = AlwaysPassChecker;
    let change = Change::new("c", "d");
    let result = checker.check(&change);
    assert!(result.passed);
    assert_eq!(result.detail, "always pass");
}

#[test]
fn test_checker_always_fail() {
    let checker = AlwaysFailChecker;
    let change = Change::new("c", "d");
    let result = checker.check(&change);
    assert!(!result.passed);
    assert_eq!(result.detail, "always fail");
}

#[test]
fn test_verdict_matches() {
    assert!(matches!(Verdict::Approved, Verdict::Approved));
    assert!(matches!(Verdict::Rejected, Verdict::Rejected));
    assert!(matches!(Verdict::Pending, Verdict::Pending));
}
