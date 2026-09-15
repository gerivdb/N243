#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
filter.py — N243 Filter

Rôle :
- Filtrer des collections selon des critères simples
- Appliquer des filtres prédéfinis ou personnalisés
- Publier un rapport de filtrage
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional


@dataclass
class FilterResult:
    item: Any
    matched: bool
    reason: str
    timestamp: str


class Filter:
    def __init__(self) -> None:
        self.results: List[FilterResult] = []

    def apply(self, items: List[Any], predicate: Callable[[Any], bool], reason: str = "matched") -> List[Any]:
        matched = []
        for item in items:
            ok = predicate(item)
            self.results.append(FilterResult(
                item=item,
                matched=ok,
                reason=reason if ok else "no match",
                timestamp=datetime.now(timezone.utc).isoformat(),
            ))
            if ok:
                matched.append(item)
        return matched

    def report(self) -> Dict[str, Any]:
        return {
            "total": len(self.results),
            "matched": sum(1 for r in self.results if r.matched),
            "results": [
                {
                    "item": r.item,
                    "matched": r.matched,
                    "reason": r.reason,
                    "timestamp": r.timestamp,
                }
                for r in self.results
            ],
        }
