#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
trigger_utils.py — N243 Trigger Utils

Rôle :
- Fournir un outil de déclenchement simple
- Vérifier si une condition est remplie
- Publier un rapport de déclenchement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class TriggerReport:
    triggered: int
    timestamp: str


class TriggerUtils:
    @staticmethod
    def evaluate(values: List[float], threshold: float) -> TriggerReport:
        triggered = sum(1 for value in values if value >= threshold)
        return TriggerReport(
            triggered=triggered,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
