#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scale_utils.py — N243 Scale Utils

Rôle :
- Fournir un outil de mise à l'échelle simple
- Publier un rapport de mise à l'échelle
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ScaleReport:
    scaled: List[float]
    timestamp: str


class ScaleUtils:
    @staticmethod
    def apply(values: List[float], factor: float) -> ScaleReport:
        scaled = [value * factor for value in values]
        return ScaleReport(
            scaled=scaled,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
