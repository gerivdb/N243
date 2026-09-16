#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
counter_utils.py — N24 N243 Counter Utils

Rôle :
- Fournir un outil simple de comptage
- Publier un rapport de compteurs
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class CounterReport:
    counters: List[str]
    timestamp: str


class CounterUtils:
    @staticmethod
    def inspect(counters: List[str]) -> CounterReport:
        return CounterReport(
            counters=list(counters),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
