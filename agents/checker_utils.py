#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
checker_utils.py — N243 Checker Utils

Rôle :
- Fournir un vérificateur simple pour des conditions
- Évaluer des prédicats et produire un rapport
- Publier un résultat de vérification
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: str
    timestamp: str


class CheckerUtils:
    def check(self, name: str, condition: Callable[[], bool], detail: str = "") -> CheckResult:
        passed = False
        try:
            passed = bool(condition())
        except Exception as exc:  # noqa: BLE001
            detail = detail or str(exc)
        return CheckResult(
            name=name,
            passed=passed,
            detail=detail,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def run(self, checks: Dict[str, Callable[[], bool]]) -> List[CheckResult]:
        results: List[CheckResult] = []
        for name, condition in checks.items():
            results.append(self.check(name, condition))
        return results
