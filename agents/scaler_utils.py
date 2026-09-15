#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scaler_utils.py — N243 Scaler Utils

Rôle :
- Fournir un outil de mise à l'échelle simple
- Normaliser des valeurs entre min et max
- Publier un rapport de mise à l'échelle
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class ScaleReport:
    scaled: List[float]
    timestamp: str


class ScalerUtils:
    @staticmethod
    def min_max(values: List[float], target_min: float = 0.0, target_max: float = 1.0) -> List[float]:
        if not values:
            return []
        min_val = min(values)
        max_val = max(values)
        if max_val == min_val:
            return [target_min] * len(values)
        return [target_min + (value - min_val) * (target_max - target_min) / (max_val - min_val) for value in values]

    def report(self, values: List[float]) -> ScaleReport:
        return ScaleReport(
            scaled=self.min_max(values),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
