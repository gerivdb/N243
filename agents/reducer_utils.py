#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reducer_utils.py — N243 Reducer Utils

Rôle :
- Fournir un réducteur simple d'éléments
- Réduire une liste avec un opérateur
- Publier un rapport de réduction
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, List, Optional


@dataclass
class ReduceReport:
    operator: str
    result: Any
    timestamp: str


class ReducerUtils:
    @staticmethod
    def reduce(values: List[Any], func: Callable[[Any, Any], Any], initial: Optional[Any] = None) -> Any:
        iterator = iter(values)
        value = initial if initial is not None else next(iterator)
        for item in iterator:
            value = func(value, item)
        return value

    def report(self, operator: str, result: Any) -> ReduceReport:
        return ReduceReport(
            operator=operator,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
