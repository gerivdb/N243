#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
interpolator_utils.py — N243 Interpolator Utils

Rôle :
- Fournir un interpolateur linéaire simple
- Estimer une valeur intermédiaire
- Publier un rapport d'interpolation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List, Tuple


@dataclass
class InterpolateReport:
    x: float
    y: float
    timestamp: str


class InterpolatorUtils:
    @staticmethod
    def linear(points: List[Tuple[float, float]], x: float) -> float:
        if not points:
            return 0.0
        (x0, y0), (x1, y1) = points[0], points[-1]
        if x1 == x0:
            return y0
        return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    def report(self, points: List[Tuple[float, float]], x: float) -> InterpolateReport:
        return InterpolateReport(
            x=x,
            y=self.linear(points, x),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
