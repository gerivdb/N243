#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
search_utils.py — N243 Search Utils

Rôle :
- Fournir une recherche simple dans des collections
- find, find_all, contains
- Publier un rapport de recherche
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Iterable, List, Optional


@dataclass
class SearchReport:
    operation: str
    found: Any
    timestamp: str


class SearchUtils:
    @staticmethod
    def find(items: Iterable[Any], predicate: Callable[[Any], bool], default: Any = None) -> Any:
        for item in items:
            if predicate(item):
                return item
        return default

    @staticmethod
    def find_all(items: Iterable[Any], predicate: Callable[[Any], bool]) -> List[Any]:
        return [item for item in items if predicate(item)]

    @staticmethod
    def contains(items: Iterable[Any], predicate: Callable[[Any], bool]) -> bool:
        return any(predicate(item) for item in items)

    @staticmethod
    def report(operation: str, found: Any) -> SearchReport:
        return SearchReport(
            operation=operation,
            found=found,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
