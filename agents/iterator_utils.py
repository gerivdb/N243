#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iterator_utils.py — N243 Iterator Utils

Rôle :
- Fournir un itérateur simple par page
- Paginer une collection
- Publier un rapport d'itération
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class IteratorReport:
    page: int
    size: int
    items: List[Any]
    timestamp: str


class IteratorUtils:
    @staticmethod
    def paginate(items: List[Any], page: int, size: int) -> List[Any]:
        start = max(page - 1, 0) * size
        end = start + size
        return items[start:end]

    def report(self, page: int, size: int, items: List[Any]) -> IteratorReport:
        return IteratorReport(
            page=page,
            size=size,
            items=list(items),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
