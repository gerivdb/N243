#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
math_utils.py — N243 Math Utils

Rôle :
- Fournir des opérations mathématiques simples
- Clamp, moyenne, arrondi (bas/haut)
- Publier un rapport mathématique
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class MathReport:
    operation: str
    value: float
    timestamp: str


class MathUtils:
    @staticmethod
    def clamp(value: float, min_val: float, max_val: float) -> float:
        if value < min_val:
            return min_val
        if value > max_val:
            return max_val
        return value

    @staticmethod
    def average(values: List[float]) -> float:
        if not values:
            return 0.0
        return sum(values) / len(values)

    @staticmethod
    def round_down(value: float, digits: int = 0) -> float:
        factor = 10 ** digits
        return math.floor(value * factor) / factor

    @staticmethod
    def round_up(value: float, digits: int = 0) -> float:
        factor = 10 ** digits
        return math.ceil(value * factor) / factor

    @staticmethod
    def report(operation: str, value: float) -> MathReport:
        return MathReport(
            operation=operation,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
