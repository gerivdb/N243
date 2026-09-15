#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
multiplier_utils.py — N243 Multiplier Utils

Rôle :
- Fournir une multiplication simple
- Multiplier des nombres ou des listes
- Publier un rapport de multiplication
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class MultiplyResult:
    inputs: List[Any]
    result: Any
    timestamp: str


class MultiplierUtils:
    @staticmethod
    def multiply_numbers(values: List[float], default: float = 1.0) -> float:
        if not values:
            return default
        result = 1.0
        for value in values:
            result *= value
        return result

    @staticmethod
    def multiply_lists(left: List[Any], right: List[Any]) -> List[Any]:
        return [str(l) + str(r) for l in left for r in right]

    def report(self, inputs: List[Any], result: Any) -> MultiplyResult:
        return MultiplyResult(
            inputs=list(inputs),
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
