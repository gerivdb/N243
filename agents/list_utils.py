#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
list_utils.py — N243 List Utils

Rôle :
- Fournir des utilitaires pour les listes
- Dedupliquer, aplatir, chunker des listes
- Publier un rapport de liste
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable, List


@dataclass
class ListReport:
    operation: str
    timestamp: str
    result: List[Any] = field(default_factory=list)


class ListUtils:
    @staticmethod
    def unique(items: Iterable[Any]) -> List[Any]:
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    @staticmethod
    def flatten(nested: Iterable[Iterable[Any]]) -> List[Any]:
        return [item for sub in nested for item in sub]

    @staticmethod
    def chunk(items: List[Any], size: int) -> List[List[Any]]:
        return [items[i : i + size] for i in range(0, len(items), size)]

    @staticmethod
    def report(operation: str, result: List[Any]) -> ListReport:
        return ListReport(
            operation=operation,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
