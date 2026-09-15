#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
counter_utils.py — N243 Counter Utils

Rôle :
- Fournir un compteur simple et borné
- Incrémenter, décrémenter, réinitialiser
- Publier un rapport d'état
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional


@dataclass
class CounterResult:
    operation: str
    value: int
    timestamp: str


class CounterUtils:
    def __init__(self, start: int = 0, min_value: Optional[int] = None, max_value: Optional[int] = None) -> None:
        self._value = start
        self._min = min_value
        self._max = max_value

    def inc(self, amount: int = 1) -> int:
        self._value += amount
        if self._max is not None:
            self._value = min(self._value, self._max)
        return self._value

    def dec(self, amount: int = 1) -> int:
        self._value -= amount
        if self._min is not None:
            self._value = max(self._value, self._min)
        return self._value

    def reset(self, value: int = 0) -> int:
        self._value = value
        return self._value

    def value(self) -> int:
        return self._value

    def report(self, operation: str) -> CounterResult:
        return CounterResult(
            operation=operation,
            value=self._value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
