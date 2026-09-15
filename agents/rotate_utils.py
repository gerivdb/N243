#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rotate_utils.py — N243 Rotate Utils

Rôle :
- Fournir un outil de rotation simple
- Publier un rapport de rotation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class RotateReport:
    rotated: List[Any]
    timestamp: str


class RotateUtils:
    @staticmethod
    def apply(values: List[Any], steps: int) -> RotateReport:
        length = len(values)
        rotated = [values[(index - steps) % length] for index in range(length)]
        return RotateReport(
            rotated=rotated,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
