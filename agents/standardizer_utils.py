#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
standardizer_utils.py — N243 Standardizer Utils

Rôle :
- Fournir un outil de standardisation simple
- Centrer et réduire des valeurs
- Publier un rapport de standardisation
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class StandardizeReport:
    standardized: List[float]
    timestamp: str


class StandardizerUtils:
    @staticmethod
    def z_score(values: List[float]) -> List[float]:
        if not values:
            return []
        mean = sum(values) / len(values)
        variance = sum((value - mean) ** 2 for value in values) / len(values)
        std = math.sqrt(variance)
        if std == 0:
            return [0.0] * len(values)
        return [(value - mean) / std for value in values]

    def report(self, values: List[float]) -> StandardizeReport:
        return StandardizeReport(
            standardized=self.z_score(values),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
