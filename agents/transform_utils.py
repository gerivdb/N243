#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transform_utils.py — N243 Transform Utils

Rôle :
- Fournir des transformations simples sur les collections
- Mapper, filtrer, réduire
- Publier un rapport de transformation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, List


@dataclass
class TransformResult:
    operation: str
    input_count: int
    output_count: int
    output: List[Any]
    timestamp: str


class TransformUtils:
    @staticmethod
    def map_items(items: List[Any], func: Callable[[Any], Any]) -> List[Any]:
        return [func(item) for item in items]

    @staticmethod
    def filter_items(items: List[Any], func: Callable[[Any], bool]) -> List[Any]:
        return [item for item in items if func(item)]

    @staticmethod
    def reduce_items(items: List[Any], func: Callable[[Any, Any], Any], initial: Any = None) -> Any:
        if not items:
            return initial
        result = initial if initial is not None else items[0]
        start = 0 if initial is not None else 1
        for item in items[start:]:
            result = func(result, item)
        return result

    def report(self, operation: str, input_count: int, output_count: int, output: List[Any]) -> TransformResult:
        return TransformResult(
            operation=operation,
            input_count=input_count,
            output_count=output_count,
            output=output,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
