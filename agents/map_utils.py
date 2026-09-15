#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
map_utils.py — N243 Map Utils

Rôle :
- Fournir un outil de mapping simple
- Publier un rapport de mapping
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass
class MapReport:
    mapped: List[Any]
    timestamp: str


class MapUtils:
    @staticmethod
    def apply(values: List[Any], func: Callable[[Any], Any]) -> MapReport:
        return MapReport(
            mapped=[func(value) for value in values],
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
