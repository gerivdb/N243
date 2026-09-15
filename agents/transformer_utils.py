#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transformer_utils.py — N243 Transformer Utils

Rôle :
- Fournir un transformateur simple pour des valeurs
- Appliquer une transformation et publier un rapport
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, List


@dataclass
class TransformReport:
    operation: str
    input_count: int
    output_count: int
    output: List[Any]
    timestamp: str


class TransformerUtils:
    @staticmethod
    def map_items(items: List[Any], func: Callable[[Any], Any]) -> List[Any]:
        return [func(item) for item in items]

    @staticmethod
    def filter_items(items: List[Any], func: Callable[[Any], bool]) -> List[Any]:
        return [item for item in items if func(item)]

    def report(self, operation: str, input_count: int, output_count: int, output: List[Any]) -> TransformReport:
        return TransformReport(
            operation=operation,
            input_count=input_count,
            output_count=output_count,
            output=output,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
