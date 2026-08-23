# PRD-001 - Event Schema & Kinds L*

**Version** : 1.0
**Statut** : DRAFT
**IntentHash** : 0xPRD001_20260801
**ADR lie** : ADR-2026-08-01-002-n243-meta-engine.md

---

## 1. Contexte

N243 étend le modèle événementiel WAZAA avec des concepts L* :
- **Runners cognitifs** (LLUX, RLM-243, TIMX, ROOTX, TLM-CORE)
- **Logique ternaire** (APPROUVE / SUSPEND / REJETTE)
- **WAL ternaire** (CONVERGENCE / DIVERGENCE / OSCILLATION)
- **Persona-Verses** (55 artefacts mythologiques N4->N7)
- **VFT** (VERSES Fractal Ternary, 3 niveaux)

Ces concepts necessitent de nouveaux **kinds Nostr** pour etre representes dans le relay.

---

## 2. Nouveaux Kinds Nostr pour N243

| Kind | Nom | Description | Structure |
|------|-----|-------------|-----------|
| **40050** | `runner-status` | Etat d'un runner L* | `{ runner, status, latency_ms }` |
| **40051** | `runner-invocation` | Invocation d'un runner | `{ runner, input, output }` |
| **40052** | `ternary-decision` | Decision ternaire | `{ decision, expert, phase }` |
| **40053** | `ternary-wal` | Entree WAL ternaire | `{ state, previous, timestamp }` |
| **40054** | `persona-verse` | Persona-Verse invoque | `{ persona, trigger }` |
| **40055** | `vft-level` | Niveau VFT (fractal) | `{ level, experts, sub_experts }` |
| **40056** | `bdcp-enforcement` | Evenement BDCP | `{ action, reason, repo }` |
| **40057** | `community-stratum` | Strate L* d'une community | `{ community, stratum }` |

---

## 3. Extension des Kinds Existants (WAZAA)

| Kind WAZAA | Extension L* | Description |
|-----------|--------------|-------------|
| **1** (text) | `kind: 1, lstar: true` | Message avec source L* |
| **42** (metadata) | `kind: 42, lstar: string` | Metadonnees runner |
| **30000** (workflow) | `kind: 30000, action: ternary` | Workflow ternaire |

---

## 4. Structure d'Evenement N243 (exemple)

```json
{
  id: 0xabc123...,
  pubkey: npub1...,
  kind: 40052,
  content: {
    decision: approve,
    expert: Architect,
    phase: CONFRONTATION,
    reasoning: Bellard challenge resolved,
    ternary_state: convergence
  },
  tags: [
    [e, 0xdef456...],
    [p, npub2...],
    [lstar, ternary-decision],
    [stratum, L1-INFRA]
  ],
  created_at: 1722500000,
  sig: ...
}
```

---

## 5. Validation

| Check | Commande |
|-------|----------|
| Validation kinds | registre N243 (`src/schemas.rs`) doit inclure les nouveaux kinds |
| Validation store | store événements WAZAA (`data/`) doit porter les index |
| Audit WAL | `../WAZAA/src/wal_event_emitter.py` doit logger les événements L* |
| KIVA-CI | python scripts/validate_meta_design.py |

---

## 6. Prochaines Etapes

1. PRD-002 : Runner Protocol
2. PRD-003 : Ternary Workflow Actions
3. PRD-004 : Ternary WAL
4. PRD-005 : BDCP Enforcement

---

## 7. References

- NIP-01 : Nostr event format
- ADR-2026-08-01-002 : N243 Meta-Engine Architecture
- VERSES : D:/DO/WEB/TOOLS/L1-INFRA/VERSES/
- Registre kinds : `src/schemas.rs`
