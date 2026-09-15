#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
predictor_utils.py — N243 Predictor Utils

Rôle :
- Fournir un prédicteur simple par tendance
- Estimer le prochain point d'une série
- Publier un rapport de prédiction
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class PredictReport:
    last: float
    next: float
    timestamp: str


class PredictorUtils:
    @staticmethod
    def predict(series: List[float]) -> float:
        if not series:
            return 0.0
        return series[-1]

    def report(self, series: List[float]) -> PredictReport:
        return PredictReport(
            last=series[-1] if series else 0.0,
            next=self.predict(series),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
