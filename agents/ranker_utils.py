#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ranker_utils.py — N243 Ranker Utils

Rôle :
- Fournir un classeur simple de valeurs
- Trier des valeurs avec ordre et limite
- Publier un rapport de classement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class RankReport:
    count: int
    timestamp: str


class RankerUtils:
    @staticmethod
    def rank(values: List[Any], top_n: int = 5, reverse: bool = False) -> List[Any]:
        return sorted(values, reverse=reverse)[:top_n]

    def report(self, values: List[Any], top_n: int = 5) -> RankReport:
        return RankReport(
            count=min(top_n, len(values)),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
