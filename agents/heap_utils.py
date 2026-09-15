#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
heap_utils.py — N243 Heap Utils

Rôle :
- Fournir des utilitaires pour les tas/heaps
- Ajouter, extraire le min/max
- Publier un rapport simple
"""

from __future__ import annotations

import heapq
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class HeapResult:
    operation: str
    item: Any
    heap_size: int
    timestamp: str


class HeapUtils:
    def __init__(self, min_heap: bool = True) -> None:
        self._heap: List[Any] = []
        self._min_heap = min_heap

    def push(self, item: Any) -> None:
        heapq.heappush(self._heap, item if self._min_heap else -item)

    def pop(self) -> Any:
        if not self._heap:
            return None
        item = heapq.heappop(self._heap)
        return item if self._min_heap else -item

    def peek(self) -> Any:
        if not self._heap:
            return None
        item = self._heap[0]
        return item if self._min_heap else -item

    def report(self, operation: str, item: Any) -> HeapResult:
        return HeapResult(
            operation=operation,
            item=item,
            heap_size=len(self._heap),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
