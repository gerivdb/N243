#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ordered_utils.py — N243 Ordered Utils

Rôle :
- Fournir des utilitaires pour les structures ordonnées
- Trier, inverser, dédupliquer tout en conservant l'ordre
- Publier un rapport simple
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class OrderedResult:
    operation: str
    input_count: int
    output_count: int
    result: List[Any]
    timestamp: str


class OrderedUtils:
    def sort_unique(self, items: List[Any]) -> List[Any]:
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return sorted(result)

    def reverse(self, items: List[Any]) -> List[Any]:
        return list(reversed(items))

    def report(self, operation: str, input_count: int, output_count: int, result: List[Any]) -> OrderedResult:
        return OrderedResult(
            operation=operation,
            input_count=input_count,
            output_count=output_count,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
