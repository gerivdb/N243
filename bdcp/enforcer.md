# PRD-005 - BDCP Enforcement

**Version** : 1.0
**Statut** : DRAFT
**IntentHash** : 0xPRD005_20260801
**ADR lie** : ADR-2026-08-01-002-n243-meta-engine.md

---

## 1. Contexte

BDCP (Blind Distributed Clone Prevention) :
- Intercepte les clones
- Valide via `known_repositories.yaml`
- Autorise ou bloque

---

## 2. Architecture

Clone Request -> BDCP Check -> known_repositories.yaml -> Approve/Block

---

## 3. BDCP Check Logic

```rust
pub struct BDCPChecker {
    known_repos: HashMap<String, RepoEntry>,
}

impl BDCPChecker {
    pub fn check_clone(&self, repo_name: &str, target_path: &Path) -> Result<(), BDCPError> {
        if !self.known_repos.contains_key(repo_name) {
            return Err(BDCPError::RepoNotDeclared(repo_name.to_string()));
        }
        // ...
    }
}
```

---

## 4. Evenements BDCP

| Kind | Nom | Description |
|------|-----|-------------|
| **40056** | `bdcp-enforcement` | Clone bloque/autorisation/erreur |

---

## 5. Validation

| Check | Commande |
|-------|----------|
| BDCP check | Tests unitaires |
| Nostr events | Kind 40056 |

---

## 6. References

- **buzz-auth** : `crates/buzz-auth/src/lib.rs`
- **ADR-032** : Clone Governance
- **PRD-001** : Event Schema
