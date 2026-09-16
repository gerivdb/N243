#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sorter_utils.py — N243 Sorter Utils

Rôle :
- Fournir un tri simple de listes
- sort_asc, sort_desc, sort_by
- Publier un rapport de tri
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, List


@dataclass
class SorterReport:
    operation: str
    timestamp: str
    result: List[Any] = field(default_factory=list)


class SorterUtils:
    @staticmethod
    def sort_asc(items: List[Any]) -> List[Any]:
        return sorted(items)

    @staticmethod
    def sort_desc(items: List[Any]) -> List[Any]:
        return sorted(items, reverse=True)

    @staticmethod
    def sort_by(items: List[Any], key: Callable[[Any], Any]) -> List[Any]:
        return sorted(items, key=key)

    @staticmethod
    def report(operation: str, result: List[Any]) -> SorterReport:
        return SorterReport(
            operation=operation,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
