#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
phase_utils.py — N243 Phase Utils

Rôle :
- Fournir un outil de phase simple
- Calculer la phase d'une valeur dans un cycle
- Publier un rapport de phase
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class PhaseReport:
    phase: float
    timestamp: str


class PhaseUtils:
    @staticmethod
    def normalize(values: List[float]) -> List[float]:
        max_val = max(values) if values else 0.0
        if max_val == 0:
            return values
        return [value / max_val for value in values]

    def report(self, values: List[float]) -> PhaseReport:
        normalized = self.normalize(values)
        phase = normalized[0] if normalized else 0.0
        return PhaseReport(
            phase=phase,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
