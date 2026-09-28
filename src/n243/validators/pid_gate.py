"""N243 PID Gate validator."""

from __future__ import annotations

from pathlib import Path


def validate_pid(pid: int, citizen: str, daemon_id: str) -> dict:
    """Validate a PID against the ecosystem governance rules.

    Returns a dict with:
    - verdict: accept | review | reject
    - errors: list of blocking issues
    - warnings: list of non-blocking issues
    """
    errors = []
    warnings = []

    # Phase 1 — PID must be a positive integer
    if not isinstance(pid, int) or pid <= 0:
        errors.append("PID must be a positive integer")

    # Phase 2 — citizen and daemon_id must be non-empty
    if not citizen:
        errors.append("citizen is required")
    if not daemon_id:
        errors.append("daemon_id is required")

    if errors:
        return {"verdict": "reject", "errors": errors, "warnings": warnings}

    # Phase 3 — Check VEX registry
    try:
        from vex.registry import VEXRegistry
        from vex.daemon_manager import VEXDaemonManager
        from vex.health import VEXHealth

        # Try common VEX config paths
        candidates = [
            Path("D:/DO/WEB/TOOLS/L3-CITIZENS/VEX/vex.yaml"),
            Path("C:/DevTools/vex.yaml"),
            Path("vex.yaml"),
        ]
        vex_config = next((p for p in candidates if p.exists()), None)
        if not vex_config:
            warnings.append("VEX config not found; skipping VEX validation")
        else:
            registry = VEXRegistry(vex_config)
            daemon_manager = VEXDaemonManager(registry)
            health = VEXHealth(registry, daemon_manager)

            # Check citizen exists
            if citizen not in registry.list_citizens():
                errors.append(f"citizen '{citizen}' not found in VEX registry")
            else:
                # Check daemon exists
                daemons = registry.list_daemons(citizen)
                if daemon_id not in [d.id for d in daemons]:
                    errors.append(f"daemon '{daemon_id}' not found for citizen '{citizen}'")
                else:
                    # Check window policy
                    policy = health.check_window_policy()
                    if not policy.get("ok"):
                        for v in policy.get("violations", []):
                            if v.get("actor") == f"{citizen}/{daemon_id}":
                                errors.append(f"window policy violation: {v.get('window_title')}")
    except Exception as exc:  # pragma: no cover - defensive
        warnings.append(f"VEX validation failed: {exc}")

    # Phase 4 — Determine verdict
    if errors:
        verdict = "reject"
    elif warnings:
        verdict = "review"
    else:
        verdict = "accept"

    return {"verdict": verdict, "errors": errors, "warnings": warnings}
