#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collection_utils.py — N243 Collection Utils

Rôle :
- Fournir des utilitaires pour les collections
- Grouper, compter, aplatir
- Publier un rapport de transformation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass
class CollectionResult:
    operation: str
    input_count: int
    output_count: int
    output: List[Any]
    timestamp: str


class CollectionUtils:
    @staticmethod
    def group_by(items: List[Any], func: Callable[[Any], Any]) -> Dict[Any, List[Any]]:
        grouped: Dict[Any, List[Any]] = {}
        for item in items:
            key = func(item)
            grouped.setdefault(key, []).append(item)
        return grouped

    @staticmethod
    def count_by(items: List[Any], func: Callable[[Any], Any]) -> Dict[Any, int]:
        counts: Dict[Any, int] = {}
        for item in items:
            key = func(item)
            counts[key] = counts.get(key, 0) + 1
        return counts

    @staticmethod
    def flatten(nested: List[List[Any]]) -> List[Any]:
        result: List[Any] = []
        for items in nested:
            result.extend(items)
        return result

    def report(self, operation: str, input_count: int, output_count: int, output: List[Any]) -> CollectionResult:
        return CollectionResult(
            operation=operation,
            input_count=input_count,
            output_count=output_count,
            output=output,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
