# Architecture — N243

**Dernière mise à jour :** 2026-07-31  
**Strate :** L4 — Interfaces utilisateur & Dev  
**Référence :** `STRATUM_RELAY.md` | `REPO.yaml`

---

## Posture

N243 est un **meta-orchestrateur cognitif L4** sur BUZZ-X — une couche d'orchestration
qui pilote BUZZ-X via l'API `Nostr ^1.0.0` sans embarquer de code BUZZ-X.

- Pas un fork Git de `BUZZ-X`
- Pas de code BUZZ-X embarqué
- Orchestration par événements Nostr signés
- Exécution déléguée aux runners Zig via ACP/subprocess

---

## Structure

```
N243/
├── schemas/                  ← PRD-001 : kinds Nostr personnalisés
├── agents/                   ← PRD-002 : protocole runner
├── workflows/                ← PRD-003 : actions ternaires
├── wal/                      ← PRD-004 : WAL ternaire
├── bdcp/                     ← PRD-005 : enforcement BDCP
├── patches/                  ← Proxies documentation BUZZ-X
├── src/                      ← Code Rust placeholder
├── docs/                     ← Documentation
├── tests/                    ← Tests
├── STRATUM_RELAY.md          ← Gouvernance L4
├── REPO.yaml                 ← Identité RSS-v2
├── design.yaml               ← Configuration conception
└── Cargo.toml                ← Dépendances BUZZ-X
```

---

## Dépendances

- **Upstream :** BUZZ-X, BRAIN-DOCS, SKILLS  
  (fournissent overlay Buzz@block, documentation, compétences)

- **Downstream :** Aucun pour l'instant (proposed)

- **Runtime cible :** Buzz@block (Nostr client) — via API Nostr/NIP-34

---

## Fonctionnement

N243 agit comme un **méta-orchestrateur** qui :

1. Définit les schémas d'événements Nostr personnalisés (kinds 40050-40057)
2. Pilote les runners Zig via ACP/subprocess (RunnerAdapter)
3. Implémente les actions ternaires Approve/Suspend/Reject
4. Trace l'état Convergence/Divergence/Oscillation dans un WAL
5. Valide les clones via BDCPChecker contre `known_repositories.yaml`

---

## Relation BUZZ-X ↔ N243

```
BUZZ-X (overlay Buzz@block)
    ↑
    │ API Nostr/NIP-34
    │
N243 (meta-orchestrateur)
    │
    ├── buzz-core/kinds → kinds 40050-40057
    ├── buzz-acp/runner_adapter → RunnerAdapter
    ├── buzz-workflow/ternary_actions → TernaryAction
    ├── buzz-audit/ternary_wal → TernaryWAL
    └── buzz-auth/bdcp → BDCPChecker
```

---

## Migration depuis BUZZ-X

N243 est construit sur BUZZ-X comme BUZZ-X est construit sur Buzz@block :

| Élément BUZZ-X | Équivalent N243 |
|---|---|
| Overlay Buzz@block | Meta-orchestrateur BUZZ-X |
| API Nostr/NIP-34 | API Nostr/NIP-34 + runners Zig |
| buzz-ecos-integration | n243-orchestrator |
| KiloCode (VS Code) | Buzz@block (Nostr) |
| Extension overlay | Orchestration cognitive |
