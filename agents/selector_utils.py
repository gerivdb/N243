#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
selector_utils.py — N243 Selector Utils

Rôle :
- Fournir un sélecteur simple d'éléments
- Sélectionner par prédicat
- Publier un rapport de sélection
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, List


@dataclass
class SelectReport:
    selected: int
    items: List[Any]
    timestamp: str


class SelectorUtils:
    @staticmethod
    def select(items: List[Any], func: Callable[[Any], bool]) -> List[Any]:
        return [item for item in items if func(item)]

    def report(self, items: List[Any]) -> SelectReport:
        return SelectReport(
            selected=len(items),
            items=list(items),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
