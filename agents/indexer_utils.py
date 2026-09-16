#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
indexer_utils.py — N243 Indexer Utils

Rôle :
- Fournir un indexeur simple d'éléments
- Ajouter et indexer des éléments
- Publier un rapport d'indexation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class IndexerReport:
    count: int
    first: Any
    last: Any
    timestamp: str


class IndexerUtils:
    def __init__(self) -> None:
        self._items: List[Any] = []

    def add(self, item: Any) -> None:
        self._items.append(item)

    def index(self, key: str) -> Dict[str, Any]:
        return {
            "count": len(self._items),
            "first": self._items[0] if self._items else None,
            "last": self._items[-1] if self._items else None,
        }

    def all(self) -> List[Any]:
        return list(self._items)

    def report(self) -> IndexerReport:
        return IndexerReport(
            count=len(self._items),
            first=self._items[0] if self._items else None,
            last=self._items[-1] if self._items else None,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
