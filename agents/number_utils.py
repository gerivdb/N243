#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
number_utils.py — N243 Number Utils

Rôle :
- Fournir des utilitaires numériques courants
- Clamp, moyenne, normalisation
- Publier un rapport numérique
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable


@dataclass
class NumberReport:
    operation: str
    value: float
    timestamp: str


class NumberUtils:
    @staticmethod
    def clamp(value: float, minimum: float, maximum: float) -> float:
        return max(minimum, min(maximum, value))

    @staticmethod
    def average(values: Iterable[float]) -> float:
        vals = list(values)
        if not vals:
            return 0.0
        return sum(vals) / len(vals)

    @staticmethod
    def normalize(value: float, minimum: float, maximum: float) -> float:
        if maximum == minimum:
            return 0.0
        return (value - minimum) / (maximum - minimum)

    @staticmethod
    def report(operation: str, value: float) -> NumberReport:
        return NumberReport(
            operation=operation,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
