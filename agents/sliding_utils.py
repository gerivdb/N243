#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sliding_utils.py — N243 Sliding Utils

Rôle :
- Fournir un outil de glissement simple
- Publier un rapport de glissement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class SlidingReport:
    windows: List[List[Any]]
    timestamp: str


class SlidingUtils:
    @staticmethod
    def apply(values: List[Any], size: int, step: int) -> SlidingReport:
        if size <= 0 or step <= 0:
            return SlidingReport(
                windows=[],
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
        windows = [values[index:index + size] for index in range(0, len(values) - size + 1, step)]
        return SlidingReport(
            windows=windows,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
