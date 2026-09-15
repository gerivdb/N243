#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aggregator_utils.py — N243 Aggregator Utils

Rôle :
- Fournir un agrégateur simple pour des valeurs
- Somme, moyenne, min, max
- Publier un rapport agrégé
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class AggregateResult:
    operation: str
    values: List[Any]
    result: Any
    timestamp: str


class AggregatorUtils:
    @staticmethod
    def sum_values(values: List[float]) -> float:
        return float(sum(values))

    @staticmethod
    def avg(values: List[float]) -> float:
        if not values:
            return 0.0
        return sum(values) / len(values)

    @staticmethod
    def min_max(values: List[float]) -> Dict[str, float]:
        if not values:
            return {"min": 0.0, "max": 0.0}
        return {"min": min(values), "max": max(values)}

    def report(self, operation: str, values: List[Any], result: Any) -> AggregateResult:
        return AggregateResult(
            operation=operation,
            values=values,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
