#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fold_utils.py — N243 Fold Utils

Rôle :
- Fournir un outil de pliage simple
- Publier un rapport de pliage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass
class FoldReport:
    folded: List[Any]
    timestamp: str


class FoldUtils:
    @staticmethod
    def apply(values: List[Any], func: Callable[[Any, Any], Any]) -> FoldReport:
        if len(values) <= 1:
            return FoldReport(
                folded=list(values),
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
        folded = [func(values[0], values[1])]
        for value in values[2:]:
            folded[-1] = func(folded[-1], value)
        return FoldReport(
            folded=folded,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
