#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bag_utils.py — N243 Bag Utils

Rôle :
- Fournir des utilitaires pour les bags/multisets
- Ajouter, compter, retirer des occurrences
- Publier un rapport simple
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class BagResult:
    operation: str
    item: Any
    count: int
    timestamp: str


class BagUtils:
    def __init__(self) -> None:
        self._counts: Dict[Any, int] = {}

    def add(self, item: Any, count: int = 1) -> None:
        self._counts[item] = self._counts.get(item, 0) + count

    def remove(self, item: Any, count: int = 1) -> None:
        if item not in self._counts:
            return
        self._counts[item] = self._counts[item] - count
        if self._counts[item] <= 0:
            del self._counts[item]

    def count(self, item: Any) -> int:
        return self._counts.get(item, 0)

    def items(self) -> List[Any]:
        return list(self._counts.keys())

    def report(self) -> Dict[str, Any]:
        return {
            "unique_items": len(self._counts),
            "total_count": sum(self._counts.values()),
            "counts": dict(self._counts),
        }

    def to_json(self) -> str:
        return json.dumps(self.report(), ensure_ascii=False, indent=2)
