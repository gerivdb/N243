#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compare_utils.py — N24 N243 Compare Utils

Rôle :
- Fournir un outil simple de comparaison
- Publier un rapport de comparaisons effectuées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class CompareReport:
    comparisons: List[str]
    timestamp: str


class CompareUtils:
    @staticmethod
    def inspect(comparisons: List[str]) -> CompareReport:
        return CompareReport(
            comparisons=list(comparisons),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
