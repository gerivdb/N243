#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
estimator_utils.py — N243 Estimator Utils

Rôle :
- Fournir un estimateur simple de moyenne
- Calculer une moyenne glissante
- Publier un rapport d'estimation
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class EstimateReport:
    window: int
    average: float
    timestamp: str


class EstimatorUtils:
    def __init__(self, window: int = 5):
        self.window = window
        self._values: deque[float] = deque(maxlen=window)

    def add(self, value: float) -> None:
        self._values.append(value)

    def average(self) -> float:
        if not self._values:
            return 0.0
        return sum(self._values) / len(self._values)

    def report(self) -> EstimateReport:
        return EstimateReport(
            window=self.window,
            average=self.average(),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
