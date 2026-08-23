# PRD-002 - Runner Protocol (N243 <-> LLUX/RLM-243/TIMX/ROOTX/TLM-CORE)

**Version** : 1.0
**Statut** : DRAFT
**IntentHash** : 0xPRD002_20260801
**ADR lie** : ADR-2026-08-01-002-n243-meta-engine.md

---

## 1. Contexte

N243 orchestre les runners cognitifs L* :
- **LLUX** - LLM BitNet 1.58b (Zig)
- **RLM-243** - Release Lifecycle (Zig)
- **TIMX** - Temporel / Features (Zig)
- **ROOTX** - Racines Symboliques (Zig)
- **TLM-CORE** - Logique Ternaire (Zig)

Le bus WAZAA (`../WAZAA/src/wazaa_bus.py`, port 1873, unités Intent) assure l'invocation ; `RunnerAdapter` reste la façade N243.

---

## 2. Architecture de Communication

N243 utilise **ACP** (Agent Client Protocol) pour invoquer les runners. Communication bidirectionnelle : N243 envoie des taches, les runners renvoient des evenements Nostr.

---

## 3. Runner Adapter Interface (Rust)

```rust
pub trait RunnerAdapter {
    async fn invoke(&self, input: RunnerInput) -> Result<RunnerOutput, RunnerError>;
    async fn status(&self) -> RunnerStatus;
    async fn shutdown(&self) -> Result<(), RunnerError>;
}

pub struct RunnerInput {
    pub prompt: String,
    pub context: serde_json::Value,
    pub timeout_secs: Option<u64>,
}

pub struct RunnerOutput {
    pub result: serde_json::Value,
    pub events: Vec<NostrEvent>,
    pub metrics: RunnerMetrics,
}

pub enum RunnerStatus {
    Active,
    Idle,
    Error(String),
}
```

---

## 4. Configuration ACP par Runner

```yaml
runners:
  llux:
    command: "llux"
    args: ["acp"]
    timeout_secs: 120
    max_retries: 3

  rlm243:
    command: "rlm243"
    args: ["acp"]
    timeout_secs: 300
    max_retries: 1

  timx:
    command: "timx"
    args: ["acp"]
    timeout_secs: 60
    max_retries: 5

  rootx:
    command: "rootx"
    args: ["acp"]
    timeout_secs: 180
    max_retries: 2

  tlm-core:
    command: "tlm-core"
    args: ["acp"]
    timeout_secs: 90
    max_retries: 3
```

---

## 5. Events Nostr generes

| Kind | Nom | Quand |
|------|-----|-------|
| **40050** | `runner-status` | Au demarrage/arret du runner |
| **40051** | `runner-invocation` | A chaque invocation de runner |

---

## 6. Validation

| Check | Commande |
|-------|----------|
| Bus WAZAA joignable | ping bus + tests adaptateur N243 |
| Runner availability | Verifier PATH des runners Zig |
| Nostr events | Verifier events 40050-40051 |

---

## 7. References

- **Bus WAZAA** : `../WAZAA/src/wazaa_bus.py`
- **PRD-001** : Event Schema & Kinds L*
- **ADR-2026-08-01-002** : N243 Meta-Engine Architecture
