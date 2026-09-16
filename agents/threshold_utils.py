#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
threshold_utils.py — N243 Threshold Utils

Rôle :
- Fournir une gestion simple de seuils
- exceeds, below, in_range, evaluate
- Publier un rapport de seuil
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, Optional


@dataclass
class ThresholdReport:
    value: float
    rules: Dict[str, float]
    status: str
    timestamp: str


class ThresholdUtils:
    @staticmethod
    def exceeds(value: float, threshold: float) -> bool:
        return value > threshold

    @staticmethod
    def below(value: float, threshold: float) -> bool:
        return value < threshold

    @staticmethod
    def in_range(value: float, min_val: float, max_val: float) -> bool:
        return min_val <= value <= max_val

    @staticmethod
    def evaluate(value: float, rules: Dict[str, float]) -> Optional[str]:
        if "min" in rules and value < rules["min"]:
            return "below_min"
        if "max" in rules and value > rules["max"]:
            return "above_max"
        return "ok"

    @staticmethod
    def report(value: float, rules: Dict[str, float]) -> ThresholdReport:
        return ThresholdReport(
            value=value,
            rules=rules,
            status=ThresholdUtils.evaluate(value, rules) or "ok",
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
