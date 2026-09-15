#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
route_utils.py — N243 Route Utils

Rôle :
- Fournir un outil de routage simple
- Sélectionner une valeur par index
- Publier un rapport de routage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class RouteReport:
    selected: Any
    index: int
    timestamp: str


class RouteUtils:
    @staticmethod
    def select(values: List[Any], index: int) -> RouteReport:
        selected = values[index]
        return RouteReport(
            selected=selected,
            index=index,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
