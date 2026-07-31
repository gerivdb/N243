# Relation N243 ↔ BUZZ-X

**Date** : 2026-07-31  
**Auteur** : N243 Engineering  
**Objet** : Vue N243 vers BUZZ-X — orchestration ↔ overlay

---

## 1. Vue N243

N243 voit BUZZ-X comme l’**overlay Nostr local**.  
Toute décision N243 est matérialisée par :
- publication d’événements Nostr via BUZZ-X
- exécution de runners Zig via ACP
- traçabilité WAL ternaire partagé

---

## 2. Flux canonical

```
Décision N243
  → publish BUZZ-X event (kind orchestré)
    → Buzz@block stocke / relay diffuse
      → WAZAA / humains reçoivent
```

---

## 3. Vérification croisée

| Vérification | Résultat |
|---|---|
| N243 dépend de BUZZ-X dans `REPO.yaml` | ✅ |
| BUZZ-X documente l’intégration N243 | ✅ (`docs/n243-integration.md`) |
| WAZAA bridge vers BUZZ-X opérationnel | ✅ 11/11 tests |
| Branche WAZAA poussée | ✅ `feat/rlm-wazaa` |

---

*Document généré le 2026-07-31 — session CTULU Phase 28 / N243 Phase 1*
