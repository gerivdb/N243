# prd_moc_supervisor.md — N243 Runner

## Rôle
Runner N243 qui supervise la gouvernance PRD↔MOC.
Reçoit les verdicts VERSES, applique la logique ternaire, et enregistre l'exécution dans le WAL ternaire.

## Déclencheurs WAZAA

| Event | Action |
|-------|--------|
| `prd.moc.validated` | Traiter le verdict VERSES |
| `prd.moc.executed` | Enregistrer `execution_trace` |
| `prd.moc.failed` | Enregistrer `failure_trace` |

## Logique ternaire

| Verdict VERSES | Action N243 |
|----------------|-------------|
| APPROUVER | Exécuter l'action, enregistrer `execution_trace` |
| SUSPENDRE | Mettre en attente, notifier OBS |
| REJETER | Archiver, enregistrer `rejection_trace` |

## WAL Ternaire

```
[APPROUVER]   → prd_moc_supervisor → execution_trace
[SUSPENDRE]   → prd_moc_supervisor → pending_queue
[REJETER]     → prd_moc_supervisor → rejection_trace
```

## Intégration
- WAZAA bus : `D:\DO\WEB\TOOLS\L4-TOOLS\WAZAA`
- KG-L trace : `D:\DO\WEB\TOOLS\L4-TOOLS\KG-L`
- PRD-MOC : `PRD-MOC-N243-SUPERVISOR-MASTER.md`
- Semantic combos : `PRD-MOC-GEN-083-semantic-combos-catalog-20260917.md` (`proposed`)
- Ontology gate : `ontology-term-gate` combo (strict mode)
