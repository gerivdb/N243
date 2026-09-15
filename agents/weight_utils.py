#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
weight_utils.py — N243 Weight Utils

Rôle :
- Fournir un outil de pondération simple
- Appliquer des poids à une liste de valeurs
- Publier un rapport de pondération
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class WeightReport:
    weighted_sum: float
    timestamp: str


class WeightUtils:
    @staticmethod
    def apply(values: List[float], weights: List[float]) -> List[float]:
        if len(values) != len(weights):
            raise ValueError("values and weights must have the same length")
        return [value * weight for value, weight in zip(values, weights)]

    def report(self, values: List[float], weights: List[float]) -> WeightReport:
        weighted = self.apply(values, weights)
        return WeightReport(
            weighted_sum=sum(weighted),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
