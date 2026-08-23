# PRD-003 - Ternary Workflow Actions

**Version** : 1.0
**Statut** : DRAFT
**IntentHash** : 0xPRD003_20260801
**ADR lie** : ADR-2026-08-01-002-n243-meta-engine.md

---

## 1. Contexte

N243 implémente les actions ternaires L* dans son moteur (`src/workflows.rs`) :
- **APPROUVE** (1.0) - validation
- **SUSPEND** (0.5) - conditionnel
- **REJETTE** (0.0) - veto

---

## 2. Actions Ternaires

### ApproveAction
```yaml
- action: approve
  condition: "runner_output.valid == true"
  approve_message: "Approuvé par ${expert}"
```

### SuspendAction
```yaml
- action: suspend
  condition: "needs_more_info == true"
  suspend_message: "En attente de ${topic}"
  timeout_secs: 3600
```

### RejectAction
```yaml
- action: reject
  condition: "veto_detected == true"
  reject_message: "Rejeté : ${reason}"
  rollback_plan: "rollback_via_mdu"
```

---

## 3. Exemple Workflow

```yaml
name: "ternary-decision"
steps:
  - action: call_runner
    runner: "oracle"
    output: oracle_result

  - action: ternary_vote
    experts: ["Architect", "Governor", "Avocat_du_Diable"]
    output: vote_result

  - action: ternary_evaluate
    votes: "${vote_result}"
    output: decision

  - action:
      approve: { action: approve }
      suspend: { action: suspend }
      reject: { action: reject }
```

---

## 4. Validation

| Check | Commande |
|-------|----------|
| Validation schéma | `src/schemas.rs` (N243WorkflowSchema) |
| Nostr events | Events 40052, 40053 |

---

## 5. References

- **Moteur workflow** : `src/workflows.rs` + `src/schemas.rs`
- **PRD-001** : Event Schema
- **PRD-002** : Runner Protocol
