---
type: PRD-MOC
version: "1.0.0"
date: "2026-09-28"
status: draft
intent_hash: 0xPRD_MOC_N243_PID_GATE_20260928
parent_prd: PRD-MOC-VEX-ECOSYSTEM-PID-GOVERNANCE-20260928.md
pole_id: POLE-MEMORY-001
owner: L3-CITIZENS
repo: gerivdb/N243
---

# PRD-MOC — N243 PID Gate

## Objectif

Valider tout PID/daemon avant acceptation dans l’écosystème gerivdb via un verdict
ternaire N243 : `accept`, `review`, `reject`.

## Contexte

N243 est le gate L3/L4 de l’écosystème. Il valide les décisions, les modèles et les
artefacts avant leur acceptation. Dans le cadre de la gouvernance PID, N243 doit :

- Recevoir une demande de validation pour chaque nouveau PID/daemon
- Vérifier la conformité avec `known_repositories.yaml`
- Vérifier que le daemon est déclaré dans `vex.yaml`
- Émettre un verdict ternaire avec traçabilité

## Décision d’architecture

N243 expose une fonction `validate_pid(pid, citizen, daemon_id, metadata)` qui :

1. Vérifie que le PID est enregistré dans VEX
2. Vérifie que le daemon est déclaré dans `vex.yaml`
3. Vérifie que le daemon est listé dans `known_repositories.yaml`
4. Émettre un verdict : `accept`, `review`, `reject`

## Plan de mise en œuvre

### Phase 1 — Contrat de validation
- [ ] Définir le schéma de validation PID
- [ ] Créer `src/n243/validators/pid_gate.py`
- [ ] Ajouter les tests unitaires

### Phase 2 — Intégration VEX
- [ ] Appeler `validate_pid()` avant `start_daemon()` dans VEX
- [ ] Si verdict != `accept` → refuser le lancement
- [ ] Tracer la décision dans VEXHealth

### Phase 3 — Observabilité
- [ ] Exposer les verdicts N243 dans `/metrics`
- [ ] Ajouter un endpoint `/health/n243-pid-gate`

## Critères d’acceptation

- [ ] `validate_pid()` retourne un verdict ternaire
- [ ] VEX refuse de lancer un daemon non validé par N243
- [ ] Les verdicts sont tracés et horodatés
- [ ] Tests passent

## Références

- **Master** : `PRD-MOC-VEX-ECOSYSTEM-PID-GOVERNANCE-20260928.md`
- **VEX** : `PRD-MOC-VEX-L3-ORCHESTRATOR-20260926.md`
- **VEX Window Policy** : `PRD-MOC-VEX-WINDOW-POLICY-20260928.md`
- **ADR** : `ADR-N243-PID-GATE-20260928.md`
- **ADR Ecosystem** : `ADR-ECOSYSTEM-PID-GOVERNANCE-20260928.md`

## Proof-of-Life

- [ ] 2026-09-28T22:35:00+02:00 — PRD-MOC créé
- [ ] 2026-09-28T22:36:00+02:00 — `validate_pid()` implémenté
- [ ] 2026-09-28T22:37:00+02:00 — Intégration VEX terminée
- [ ] 2026-09-28T22:38:00+02:00 — Tests passent
