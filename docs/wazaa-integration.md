# Relation N243 ↔ WAZAA

**Date** : 2026-07-31 (créé) / 2026-08-23 (pivot Buzz@block → WAZAA)  
**Auteur** : N243 Engineering  
**Objet** : Vue N243 vers WAZAA — supervision ↔ orchestration  
**Historique** : remplace `docs/buzz-x-integration.md` (cible Buzz@block abandonnée dans ENV2)

---

## 1. Vue N243

N243 voit WAZAA comme le **bus d'orchestration local** (`src/wazaa_bus.py`, port 1873).  
Toute décision N243 est matérialisée par :
- publication d'événements via le bus WAZAA (unités Intent)
- exécution des runners Zig (LLUX, RLM-243, TIMX, ROOTX, TLM-CORE) via l'adaptateur N243
- traçabilité WAL ternaire partagée (états Convergence/Divergence/Oscillation)

---

## 2. Flux canonique

```
Décision N243 (ternaire APPROUVER/SUSPENDRE/REJETER)
  → publish event bus WAZAA (Intent orchestré)
    → WAL append-only consigné (wal_event_emitter.py)
      → runners Zig invoqués / KiloCode (MCP) reçoit
```

---

## 3. Vérification croisée

| Vérification | Résultat |
|---|---|
| N243 déclare WAZAA en dépendance upstream (`REPO.yaml`) | ✅ |
| N243 déclaré dans la SOT (`known_repositories.yaml`) | ✅ 2026-08-23 |
| Bus WAZAA joignable depuis l'adaptateur N243 | 🔲 à valider (Sprint 2 INTENT V0.5) |
| Pipeline KG-L → WAZAA → N243 → MCP | 🔲 Sprint 2-3 |

---

*Document généré le 2026-07-31 — session CTULU Phase 28 / N243 Phase 1. Pivot WAZAA appliqué le 2026-08-23.*
