#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
harmonic_utils.py — N243 Harmonic Utils

Rôle :
- Fournir un outil harmonique simple
- Calculer la moyenne harmonique
- Publier un rapport harmonique
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class HarmonicReport:
    harmonic_mean: float
    timestamp: str


class HarmonicUtils:
    @staticmethod
    def mean(values: List[float]) -> float:
        if not values or any(value == 0 for value in values):
            return 0.0
        return len(values) / sum(1.0 / value for value in values)

    def report(self, values: List[float]) -> HarmonicReport:
        return HarmonicReport(
            harmonic_mean=self.mean(values),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
