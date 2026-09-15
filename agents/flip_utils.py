#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
flip_utils.py — N243 Flip Utils

Rôle :
- Fournir un outil de retournement simple
- Publier un rapport de retournement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class FlipReport:
    flipped: List[Any]
    timestamp: str


class FlipUtils:
    @staticmethod
    def apply(values: List[Any]) -> FlipReport:
        flipped = list(reversed(values))
        return FlipReport(
            flipped=flipped,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
