#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gate_utils.py — N243 Gate Utils

Rôle :
- Fournir un outil de seuil simple
- Vérifier si une valeur passe un seuil
- Publier un rapport de passage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class GateReport:
    passed: int
    failed: int
    timestamp: str


class GateUtils:
    @staticmethod
    def check(values: List[float], threshold: float) -> GateReport:
        passed = sum(1 for value in values if value >= threshold)
        return GateReport(
            passed=passed,
            failed=len(values) - passed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
