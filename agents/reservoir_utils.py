#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reservoir_utils.py — N243 Reservoir Utils

Rôle :
- Fournir un réservoir simple de valeurs
- Ajouter et prélever des valeurs
- Publier un rapport de réservoir
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class ReservoirReport:
    capacity: int
    count: int
    items: List[Any]
    timestamp: str


class ReservoirUtils:
    def __init__(self, capacity: int = 10) -> None:
        self._capacity = capacity
        self._items: List[Any] = []

    def add(self, item: Any) -> bool:
        if len(self._items) >= self._capacity:
            return False
        self._items.append(item)
        return True

    def take(self) -> Any:
        if not self._items:
            return None
        return self._items.pop(0)

    def report(self) -> ReservoirReport:
        return ReservoirReport(
            capacity=self._capacity,
            count=len(self._items),
            items=list(self._items),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
