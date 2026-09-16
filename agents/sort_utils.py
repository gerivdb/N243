#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sort_utils.py — N24 N243 Sort Utils

Rôle :
- Fournir un outil simple de tri
- Publier un rapport de collections triées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class SortReport:
    sorted_items: List[str]
    timestamp: str


class SortUtils:
    @staticmethod
    def inspect(items: List[str]) -> SortReport:
        return SortReport(
            sorted_items=sorted(items),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
