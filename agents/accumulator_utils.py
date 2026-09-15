#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
accumulator_utils.py — N243 Accumulator Utils

Rôle :
- Fournir un accumulateur simple de valeurs
- Ajouter des valeurs et obtenir le cumul
- Publier un rapport d'accumulation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class AccumulatorReport:
    count: int
    total: Any
    timestamp: str


class AccumulatorUtils:
    def __init__(self, start: Any = 0) -> None:
        self._total = start
        self._count = 0

    def add(self, value: Any) -> None:
        self._total += value
        self._count += 1

    def total(self) -> Any:
        return self._total

    def count(self) -> int:
        return self._count

    def report(self) -> AccumulatorReport:
        return AccumulatorReport(
            count=self._count,
            total=self._total,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
