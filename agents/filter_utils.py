#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
filter_utils.py — N243 Filter Utils

Rôle :
- Fournir un filtre simple pour des collections
- Inclure/exclure selon un prédicat
- Publier un rapport de filtrage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, List


@dataclass
class FilterResult:
    operation: str
    input_count: int
    output_count: int
    output: List[Any]
    timestamp: str


class FilterUtils:
    @staticmethod
    def include(items: List[Any], func: Callable[[Any], bool]) -> List[Any]:
        return [item for item in items if func(item)]

    @staticmethod
    def exclude(items: List[Any], func: Callable[[Any], bool]) -> List[Any]:
        return [item for item in items if not func(item)]

    def report(self, operation: str, input_count: int, output_count: int, output: List[Any]) -> FilterResult:
        return FilterResult(
            operation=operation,
            input_count=input_count,
            output_count=output_count,
            output=output,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
