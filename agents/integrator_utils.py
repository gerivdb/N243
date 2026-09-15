#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
integrator_utils.py — N243 Integrator Utils

Rôle :
- Fournir un intégrateur simple par somme cumulative
- Intégrer une série de valeurs
- Publier un rapport d'intégration
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class IntegrateReport:
    total: float
    timestamp: str


class IntegratorUtils:
    @staticmethod
    def cumulative_sum(values: List[float]) -> List[float]:
        result: List[float] = []
        total = 0.0
        for value in values:
            total += value
            result.append(total)
        return result

    def report(self, values: List[float]) -> IntegrateReport:
        return IntegrateReport(
            total=values[-1] if values else 0.0,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
