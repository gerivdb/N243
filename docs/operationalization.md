# N243 — Documentation Opérationnelle

> **IntentHash** : `0xN243_OPERATIONALIZATION_20260915`
> **Version** : 1.0.0
> **Date** : 2026-09-15

## 1. Architecture

N243 est le **méta-orchestrateur cognitif** de l'écosystème gerivdb. Il supervise
l'exécution des pipelines ML/IA via une logique ternaire (APPROUVER / SUSPENDRE / REJETER).

### 1.1 Composants

| Composant | Description | Fichier |
|-----------|-------------|---------|
| **Agents** | 4 agents KG-L spécialisés | `src/agents.rs` |
| **Workflows** | Pipelines ML orchestres | `workflows/*/n243-*.yaml` |
| **WAL** | Write-Ahead Log | `src/wal/*.rs` |
| **Gates** | Validation GF/L5/L6 | `src/gates/*.rs` |
| **BDCP** | Mode réseau sécurisé | `src/bdcp/*.rs` |
| **WAZAA Bridge** | Publication événementielle | `src/bridge/wazaa_bridge.rs` |
| **VOLTX Bridge** | Bus unifié 5 canaux | `src/bridge/voltx_bridge.rs` |

### 1.2 Agents KG-L

| Agent | Axe KG-L | Rôle |
|-------|----------|------|
| `LluxAgent` | Axe 17 | Transformer Memory |
| `TimxAgent` | Axe 9 | Dynamic Systems |
| `RootxAgent` | Axe 13 | Ontologies |
| `TlmAgent` | Axe 12 | Ternary Logic |

### 1.3 Workflows

| Workflow | Description | Fichier |
|----------|-------------|---------|
| `kg_mutation` | Mutation du Knowledge Graph | `workflows/kg_mutation/n243-kg-mutation.yaml` |
| `ml_train` | Entraînement de modèles ML | `workflows/ml_train/n243-ml-train.yaml` |

## 2. Bridges

### 2.1 WAZAA Bridge

Le WAZAA Bridge permet la publication et la souscription sur le bus événementiel WAZAA.

```rust
use n243::bridge::wazaa_bridge::{WazaaBridge, WazaaMessage};

let mut bridge = WazaaBridge::new();
bridge.connect()?;
bridge.publish("topic", "payload")?;
bridge.subscribe("topic", |msg| { /* handler */ })?;
```

### 2.2 VOLTX Bridge

Le VOLTX Bridge expose 5 canaux intégrés :

| Canal | Direction | Usage |
|-------|-----------|-------|
| `PLIX` | Vision → Audio | Sonification données |
| `PIANO` | Audio → Narration | Feature extraction |
| `TALEX` | Narration → Graphe | Knowledge extraction |
| `SPIDX` | Graphe → Diffusion | Model serving |
| `WAZAA` | Diffusion → Vision | Feedback loop |

```rust
use n243::bridge::voltx_bridge::{VoltxBridge, VoltxChannel};

let mut bridge = VoltxBridge::new();
bridge.connect()?;
bridge.register_channel(VoltxChannel::Plix, |msg| { /* handler */ })?;
bridge.send(VoltxChannel::Plix, "payload")?;
```

## 3. Validation

### 3.1 Tests unitaires

```bash
cargo test --lib
```

### 3.2 Tests d'intégration

```bash
pytest tests/integration/test_n243_integration.py -v
```

### 3.3 Conformité RSS-v2

```bash
python rss_lint.py --repo . --depth 4 --check-governance
```

## 4. Références

- **PRD-MOC Master** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-N243-OPERATIONALIZATION-MASTER-2026-09-15.md`
- **VOLTX Integration** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-VOLTX-N243-INTEGRATION-2026-09-15.md`
- **ML Training Pipeline** : `GOVERNANCE-HUB/PRD-MOC/general/PRD-MOC-KG-L-ML-TRAINING-PIPELINE-2026-09-15.md`
- **N243** : gerivdb/N243
