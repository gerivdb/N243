#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
splitter_utils.py — N243 Splitter Utils

Rôle :
- Fournir un découpeur simple de texte
- Découper par séparateur
- Publier un rapport de découpage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class SplitReport:
    separator: str
    parts: int
    items: List[str]
    timestamp: str


class SplitterUtils:
    @staticmethod
    def split(value: str, separator: str) -> List[str]:
        if not value:
            return []
        return value.split(separator)

    def report(self, separator: str, items: List[str]) -> SplitReport:
        return SplitReport(
            separator=separator,
            parts=len(items),
            items=list(items),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
