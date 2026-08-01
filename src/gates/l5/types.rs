// N243/gates/l5/types.rs
// Types partagés pour le L5 Trust Gate.

/// Verdict L5
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Verdict {
    Approved,
    Rejected,
    Pending,
}

impl Default for Verdict {
    fn default() -> Self {
        Verdict::Approved
    }
}

/// Changement à vérifier par le L5 Trust Gate.
pub struct Change {
    pub id: String,
    pub description: String,
    pub files: Vec<String>,
}

impl Change {
    pub fn new(id: impl Into<String>, description: impl Into<String>) -> Self {
        Self {
            id: id.into(),
            description: description.into(),
            files: Vec::new(),
        }
    }
}

/// Résultat d'un check L5.
#[derive(Debug, Clone)]
pub struct CheckResult {
    pub passed: bool,
    pub detail: String,
}

pub trait Checker {
    fn check(&self, change: &Change) -> CheckResult;
}
