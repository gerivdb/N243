#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
loop_utils.py — N243 Loop Utils

Rôle :
- Fournir des utilitaires pour les boucles et itérations
- Chunker, mapper, trouver le premier élément
- Publier un rapport de boucle
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Iterable, List


@dataclass
class LoopReport:
    operation: str
    timestamp: str
    result: List[Any] = field(default_factory=list)


class LoopUtils:
    @staticmethod
    def chunk(items: List[Any], size: int) -> List[List[Any]]:
        return [items[i : i + size] for i in range(0, len(items), size)]

    @staticmethod
    def batch_map(items: Iterable[Any], func: Callable[[Any], Any]) -> List[Any]:
        return [func(item) for item in items]

    @staticmethod
    def find_first(items: Iterable[Any], predicate: Callable[[Any], bool], default: Any = None) -> Any:
        for item in items:
            if predicate(item):
                return item
        return default

    @staticmethod
    def report(operation: str, result: List[Any]) -> LoopReport:
        return LoopReport(
            operation=operation,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
