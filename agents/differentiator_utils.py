#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
differentiator_utils.py — N243 Differentiator Utils

Rôle :
- Fournir un différentiateur simple de valeurs
- Calculer les différences entre valeurs successives
- Publier un rapport de différentiation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class DiffReport:
    diffs: List[float]
    timestamp: str


class DifferentiatorUtils:
    @staticmethod
    def diff(values: List[float]) -> List[float]:
        return [values[i] - values[i - 1] for i in range(1, len(values))]

    def report(self, values: List[float]) -> DiffReport:
        return DiffReport(
            diffs=self.diff(values),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
