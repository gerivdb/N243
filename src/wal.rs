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

    pub fn replay(&mut self, path: impl AsRef<Path>) -> std::io::Result<usize> {
        let path = path.as_ref();
        let content = fs::read_to_string(path)?;
        let mut count = 0;
        for line in content.lines() {
            let line = line.trim();
            if line.is_empty() {
                continue;
            }
            if let Ok(entry) = serde_json::from_str::<WalEntry>(line) {
                self.entries.push(entry.clone());
                self.current_states.insert(entry.entity.clone(), entry.current);
                count += 1;
            }
        }
        Ok(count)
    }

    pub fn compact(&mut self, max_entries: usize) -> usize {
        if self.entries.len() <= max_entries {
            return 0;
        }
        let remove = self.entries.len() - max_entries;
        self.entries.drain(0..remove);
        remove
    }

    pub fn compact_ttl(&mut self, ttl_days: u64) -> std::io::Result<usize> {
        let cutoff = chrono::Utc::now().timestamp() - (ttl_days * 24 * 60 * 60) as i64;
        let initial_len = self.entries.len();
        self.entries.retain(|entry| entry.timestamp >= cutoff);
        let removed = initial_len - self.entries.len();
        if removed > 0 {
            if let Some(ref path) = self.path {
                self.rewrite_file(path)?;
            }
        }
        Ok(removed)
    }

    fn append_to_file(&self, path: &str, entry: &WalEntry) -> std::io::Result<()> {
        if let Some(parent) = Path::new(path).parent() {
            fs::create_dir_all(parent)?;
        }
        let mut file = OpenOptions::new().create(true).append(true).open(path)?;
        let line = serde_json::to_string(entry).unwrap_or_default();
        writeln!(file, "{}", line)
    }

    fn rewrite_file(&self, path: &str) -> std::io::Result<()> {
        let content = self
            .entries
            .iter()
            .map(|entry| serde_json::to_string(entry).unwrap_or_default())
            .collect::<Vec<_>>()
            .join("\n");
        fs::write(path, content + "\n")
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

    #[test]
    fn test_n243_wal_replay() {
        let tmp = std::env::temp_dir().join("n243-wal-replay-test.jsonl");
        let _ = fs::write(&tmp, r#"{"entity":"replay.entity","previous":"Oscillation","current":"Convergence","reason":"replay","timestamp":0}
{"entity":"replay.entity","previous":"Convergence","current":"Divergence","reason":"replay","timestamp":1}
"#);
        let mut wal = N243WAL::new();
        let count = wal.replay(&tmp).expect("replay");
        assert_eq!(count, 2);
        assert_eq!(wal.current_state("replay.entity"), Some(&TernaryState::Divergence));
        assert_eq!(wal.history("replay.entity").len(), 2);
        let _ = fs::remove_file(&tmp);
    }

    #[test]
    fn test_n243_wal_compact() {
        let mut wal = N243WAL::new();
        wal.record("a", TernaryState::Convergence, "");
        wal.record("b", TernaryState::Oscillation, "");
        wal.record("c", TernaryState::Divergence, "");
        assert_eq!(wal.entries.len(), 3);
        let removed = wal.compact(2);
        assert_eq!(removed, 1);
        assert_eq!(wal.entries.len(), 2);
        assert_eq!(wal.entries[0].entity, "b");
        assert_eq!(wal.entries[1].entity, "c");
    }

    #[test]
    fn test_n243_wal_compact_ttl() {
        let tmp = std::env::temp_dir().join("n243-wal-compact-ttl-test.jsonl");
        let now = chrono::Utc::now().timestamp();
        let old_ts = now - (31 * 24 * 60 * 60); // 31 jours
        let fresh_ts = now;
        let _ = fs::write(
            &tmp,
            format!(
                r#"{{"entity":"old","previous":"Convergence","current":"Divergence","reason":"old","timestamp":{old_ts}}}
{{"entity":"fresh","previous":"Oscillation","current":"Convergence","reason":"fresh","timestamp":{fresh_ts}}}
"#
            ),
        );
        let mut wal = N243WAL::with_path(tmp.to_str().unwrap());
        let _ = wal.replay(&tmp);
        assert_eq!(wal.entries.len(), 2);
        let removed = wal.compact_ttl(30).expect("compact_ttl");
        assert_eq!(removed, 1);
        assert_eq!(wal.entries.len(), 1);
        assert_eq!(wal.entries[0].entity, "fresh");
        let content = fs::read_to_string(&tmp).expect("read compacted wal");
        assert!(content.contains("fresh"));
        assert!(!content.contains("old"));
        let _ = fs::remove_file(&tmp);
    }
}
