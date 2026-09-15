#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transformer_utils.py — N243 Transformer Utils

Rôle :
- Fournir un transformateur simple d'éléments
- Appliquer une fonction à chaque élément
- Publier un rapport de transformation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, List


@dataclass
class TransformReport:
    transformed: int
    items: List[Any]
    timestamp: str


class TransformerUtils:
    @staticmethod
    def transform(items: List[Any], func: Callable[[Any], Any]) -> List[Any]:
        return [func(item) for item in items]

    def report(self, items: List[Any]) -> TransformReport:
        return TransformReport(
            transformed=len(items),
            items=list(items),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
