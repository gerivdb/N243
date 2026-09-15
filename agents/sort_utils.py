#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sort_utils.py — N243 Sort Utils

Rôle :
- Fournir un outil de tri simple
- Publier un rapport de tri
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class SortReport:
    sorted: List[Any]
    timestamp: str


class SortUtils:
    @staticmethod
    def apply(values: List[Any]) -> SortReport:
        return SortReport(
            sorted=sorted(values),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
