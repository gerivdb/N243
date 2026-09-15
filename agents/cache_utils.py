#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cache_utils.py — N243 Cache Utils

Rôle :
- Fournir un cache mémoire simple
- Ajouter, récupérer, invalider des entrées
- Publier un rapport d'état du cache
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class CacheResult:
    operation: str
    key: str
    hit: bool
    timestamp: str


class CacheUtils:
    def __init__(self) -> None:
        self._items: Dict[str, Any] = {}

    def put(self, key: str, value: Any) -> None:
        self._items[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._items.get(key, default)

    def invalidate(self, key: str) -> None:
        self._items.pop(key, None)

    def keys(self) -> List[str]:
        return list(self._items.keys())

    def report(self, operation: str, key: str, hit: bool) -> CacheResult:
        return CacheResult(
            operation=operation,
            key=key,
            hit=hit,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
