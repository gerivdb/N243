#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
queue_utils.py — N243 Queue Utils

Rôle :
- Fournir une file d'attente simple
- Enfiler, défiler, consulter la tête
- Publier un rapport d'état
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List, Optional


@dataclass
class QueueResult:
    operation: str
    item: Any
    size: int
    timestamp: str


class QueueUtils:
    def __init__(self) -> None:
        self._items: List[Any] = []

    def enqueue(self, item: Any) -> None:
        self._items.append(item)

    def dequeue(self) -> Any:
        if not self._items:
            return None
        return self._items.pop(0)

    def peek(self) -> Any:
        if not self._items:
            return None
        return self._items[0]

    def size(self) -> int:
        return len(self._items)

    def report(self, operation: str, item: Any) -> QueueResult:
        return QueueResult(
            operation=operation,
            item=item,
            size=self.size(),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
