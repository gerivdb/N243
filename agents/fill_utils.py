#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fill_utils.py — N243 Fill Utils

Rôle :
- Fournir un outil de remplissage par borne simple
- Publier un rapport de remplissage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class FillReport:
    filled: List[Any]
    timestamp: str


class FillUtils:
    @staticmethod
    def apply(values: List[Any], start: int, end: int, fill: Any) -> FillReport:
        filled = list(values)
        for index in range(start, min(end, len(filled))):
            filled[index] = fill
        return FillReport(
            filled=filled,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
