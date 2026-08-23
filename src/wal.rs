// N243 — WAL (Write-Ahead Log)
// Ternary WAL N243 — sémantique append-only alignée sur WAZAA (wal_event_emitter.py).

use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::fs::{self, OpenOptions};
use std::io::Write;
use std::path::Path;

/// Ternary state for N243 WAL
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Copy)]
pub enum TernaryState {
    Convergence,
    Divergence,
    Oscillation,
}

impl TernaryState {
    pub fn to_score(&self) -> f32 {
        match self {
            TernaryState::Convergence => 1.0,
            TernaryState::Oscillation => 0.5,
            TernaryState::Divergence => 0.0,
        }
    }
}

/// WAL entry for N243
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct WalEntry {
    pub entity: String,
    pub previous: TernaryState,
    pub current: TernaryState,
    pub reason: String,
    pub timestamp: i64,
}

/// N243 WAL — Write-Ahead Log with governance tracking
#[derive(Debug, Clone, Default)]
pub struct N243WAL {
    entries: Vec<WalEntry>,
    current_states: HashMap<String, TernaryState>,
    path: Option<String>,
}

impl N243WAL {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn with_path(path: impl Into<String>) -> Self {
        Self {
            path: Some(path.into()),
            ..Self::default()
        }
    }

    pub fn record(&mut self, entity: &str, state: TernaryState, reason: &str) {
        let previous = self
            .current_states
            .get(entity)
            .copied()
            .unwrap_or(TernaryState::Oscillation);

        let entry = WalEntry {
            entity: entity.to_string(),
            previous,
            current: state,
            reason: reason.to_string(),
            timestamp: chrono::Utc::now().timestamp(),
        };

        self.entries.push(entry.clone());
        self.current_states.insert(entity.to_string(), state);

        if let Some(ref path) = self.path {
            let _ = self.append_to_file(path, &entry);
        }
    }

    pub fn current_state(&self, entity: &str) -> Option<&TernaryState> {
        self.current_states.get(entity)
    }

    pub fn history(&self, entity: &str) -> Vec<&WalEntry> {
        self.entries.iter().filter(|e| e.entity == entity).collect()
    }

    pub fn detect_oscillations(&self, entity: &str) -> Vec<(&WalEntry, &WalEntry)> {
        let mut pairs = Vec::new();
        let history: Vec<&WalEntry> = self.history(entity);
        for i in 0..history.len().saturating_sub(1) {
            let a = history[i];
            let b = history[i + 1];
            if matches!((a.current, b.current), (TernaryState::Convergence, TernaryState::Oscillation))
                || matches!((a.current, b.current), (TernaryState::Oscillation, TernaryState::Divergence))
                || matches!((a.current, b.current), (TernaryState::Divergence, TernaryState::Oscillation))
                || matches!((a.current, b.current), (TernaryState::Oscillation, TernaryState::Convergence))
            {
                pairs.push((a, b));
            }
        }
        pairs
    }

    fn append_to_file(&self, path: &str, entry: &WalEntry) -> std::io::Result<()> {
        if let Some(parent) = Path::new(path).parent() {
            fs::create_dir_all(parent)?;
        }
        let mut file = OpenOptions::new().create(true).append(true).open(path)?;
        let line = serde_json::to_string(entry).unwrap_or_default();
        writeln!(file, "{}", line)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_n243_wal_record() {
        let mut wal = N243WAL::new();
        wal.record("n243.boot", TernaryState::Convergence, "system-start");
        assert_eq!(
            wal.current_state("n243.boot"),
            Some(&TernaryState::Convergence)
        );
        assert_eq!(wal.history("n243.boot").len(), 1);
    }

    #[test]
    fn test_n243_wal_oscillation_detection() {
        let mut wal = N243WAL::new();
        wal.record("x", TernaryState::Oscillation, "");
        wal.record("x", TernaryState::Convergence, "");
        wal.record("x", TernaryState::Oscillation, "");
        let oscillations = wal.detect_oscillations("x");
        assert_eq!(oscillations.len(), 2);
    }
}
