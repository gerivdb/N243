# N243 — Meta-Orchestrateur Cognitif L*

**Version** : 0.1.0
**Statut** : DRAFT
**Strate** : L4-TOOLS
**IntentHash** : 0xN243_20260801

---

## Vision

N243 orchestre les 5 runners cognitifs core de l'écosystème L* :
- **LLUX** (BitNet 1.58b)
- **RLM-243** (Release Lifecycle)
- **TIMX** (Temporel / Features)
- **ROOTX** (Racines Symboliques)
- **TLM-CORE** (Logique Ternaire)

S'appuie sur **Buzz@block** (fork de `block/buzz`) comme infrastructure.

---

## Structure

N243/
├── Cargo.toml
├── README.md
├── schemas/
│   └── kinds-lstar.md      # PRD-001
├── agents/
│   └── runner-protocol.md  # PRD-002
├── workflows/
│   └── ternary-actions.md  # PRD-003
├── wal/
│   └── ternary-wal.md      # PRD-004
└── bdcp/
    └── enforcer.md         # PRD-005

## Dépendances

| Dépendance | Chemin | Rôle |
|------------|--------|------|
| Buzz@block | ../../BUZZ-X/Buzz@block/ | Relay, ACP, Workflow |
| LLUX | PATH | Runner LLM |
| RLM-243 | PATH | Runner Release |
| TIMX | PATH | Runner Temporel |
| ROOTX | PATH | Runner Symbolique |
| TLM-CORE | PATH | Runner Ternaire |

## Quick Start

cd D:/DO/WEB/TOOLS/L4-TOOLS/N243
cargo build
cargo run
