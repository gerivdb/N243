#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
range_utils.py — N243 Range Utils

Rôle :
- Fournir des utilitaires simples pour les intervalles numériques
- Range inclusif, range avec step, chunking
- Publier un rapport d'intervallle
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class RangeReport:
    operation: str
    timestamp: str
    result: List[Any] = field(default_factory=list)


class RangeUtils:
    @staticmethod
    def range_inclusive(start: int, end: int) -> List[int]:
        return list(range(start, end + 1))

    @staticmethod
    def step_range(start: int, end: int, step: int) -> List[int]:
        return list(range(start, end + 1, step))

    @staticmethod
    def chunks(items: List[Any], size: int) -> List[List[Any]]:
        if size <= 0:
            raise ValueError("size must be > 0")
        return [items[i:i + size] for i in range(0, len(items), size)]

    @staticmethod
    def report(operation: str, result: List[Any]) -> RangeReport:
        return RangeReport(
            operation=operation,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
