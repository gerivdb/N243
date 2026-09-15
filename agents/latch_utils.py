#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
latch_utils.py — N243 Latch Utils

Rôle :
- Fournir un outil de verrouillage simple
- Mémoriser un état de verrouillage
- Publier un rapport de verrouillage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class LatchReport:
    latched: int
    timestamp: str


class LatchUtils:
    @staticmethod
    def evaluate(values: List[float], threshold: float) -> LatchReport:
        latched = sum(1 for value in values if value >= threshold)
        return LatchReport(
            latched=latched,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
