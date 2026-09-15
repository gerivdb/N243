#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timer_utils.py — N243 Timer Utils

Rôle :
- Fournir un outil de temporisation simple
- Mesurer le temps écoulé
- Publier un rapport de temporisation
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class TimerReport:
    elapsed: float
    timestamp: str


class TimerUtils:
    @staticmethod
    def measure(values: List[float]) -> TimerReport:
        start = time.perf_counter()
        sum(values)
        elapsed = time.perf_counter() - start
        return TimerReport(
            elapsed=elapsed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
