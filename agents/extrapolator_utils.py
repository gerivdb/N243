#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extrapolator_utils.py — N243 Extrapolator Utils

Rôle :
- Fournir un extrapolateur simple par tendance
- Estimer un point au-delà de la série
- Publier un rapport d'extrapolation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ExtrapolateReport:
    last: float
    extrapolated: float
    timestamp: str


class ExtrapolatorUtils:
    @staticmethod
    def extrapolate(series: List[float], steps: int = 1) -> float:
        if len(series) < 2:
            return series[-1] if series else 0.0
        return series[-1] + steps * (series[-1] - series[-2])

    def report(self, series: List[float], steps: int = 1) -> ExtrapolateReport:
        return ExtrapolateReport(
            last=series[-1] if series else 0.0,
            extrapolated=self.extrapolate(series, steps),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
