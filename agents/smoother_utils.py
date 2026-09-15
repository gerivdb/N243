#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
smoother_utils.py — N243 Smoother Utils

Rôle :
- Fournir un lisseur simple de valeurs
- Appliquer une moyenne mobile
- Publier un rapport de lissage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class SmoothReport:
    smoothed: List[float]
    timestamp: str


class SmootherUtils:
    @staticmethod
    def moving_average(values: List[float], window: int = 3) -> List[float]:
        if window <= 0 or not values:
            return []
        result: List[float] = []
        for i in range(len(values)):
            start = max(0, i - window + 1)
            window_values = values[start : i + 1]
            result.append(sum(window_values) / len(window_values))
        return result

    def report(self, values: List[float], window: int = 3) -> SmoothReport:
        return SmoothReport(
            smoothed=self.moving_average(values, window),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
