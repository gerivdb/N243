#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hold_utils.py — N243 Hold Utils

Rôle :
- Fournir un outil de rétention simple
- Mémoriser les valeurs au-dessus d'un seuil
- Publier un rapport de rétention
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class HoldReport:
    held: List[float]
    timestamp: str


class HoldUtils:
    @staticmethod
    def filter(values: List[float], threshold: float) -> HoldReport:
        held = [value for value in values if value >= threshold]
        return HoldReport(
            held=held,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
