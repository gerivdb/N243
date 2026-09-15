#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reduce_utils.py — N243 Reduce Utils

Rôle :
- Fournir un outil de réduction simple
- Publier un rapport de réduction
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass
class ReduceReport:
    reduced: Any
    timestamp: str


class ReduceUtils:
    @staticmethod
    def apply(values: List[Any], func: Callable[[Any, Any], Any], initial: Any = None) -> ReduceReport:
        iterator = iter(values)
        accumulator = initial if initial is not None else next(iterator)
        for value in iterator:
            accumulator = func(accumulator, value)
        return ReduceReport(
            reduced=accumulator,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
