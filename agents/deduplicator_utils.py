#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deduplicator_utils.py — N243 Deduplicator Utils

Rôle :
- Fournir un dédoublonneur simple pour des listes
- Conserver l'ordre original
- Publier un rapport de dédoublonnage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class DedupResult:
    input_count: int
    output_count: int
    output: List[Any]
    timestamp: str


class DeduplicatorUtils:
    @staticmethod
    def deduplicate(items: List[Any]) -> List[Any]:
        seen: set = set()
        result: List[Any] = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    def report(self, items: List[Any]) -> DedupResult:
        output = self.deduplicate(items)
        return DedupResult(
            input_count=len(items),
            output_count=len(output),
            output=output,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
