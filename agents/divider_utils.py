#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
divider_utils.py — N243 Divider Utils

Rôle :
- Fournir une division simple de nombres
- Gérer la division par zéro
- Publier un rapport de division
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class DividerReport:
    numerator: Any
    denominator: Any
    result: Any
    success: bool
    timestamp: str


class DividerUtils:
    @staticmethod
    def divide(numerator: Any, denominator: Any, default: Any = None) -> Any:
        try:
            return numerator / denominator
        except ZeroDivisionError:
            return default

    def report(self, numerator: Any, denominator: Any, success: bool, result: Any) -> DividerReport:
        return DividerReport(
            numerator=numerator,
            denominator=denominator,
            result=result,
            success=success,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
