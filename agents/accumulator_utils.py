#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
accumulator_utils.py — N24 N243 Accumulator Utils

Rôle :
- Fournir un outil simple d'accumulation
- Publier un rapport de valeurs accumulées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class AccumulateReport:
    values: List[str]
    timestamp: str


class AccumulatorUtils:
    @staticmethod
    def inspect(values: List[str]) -> AccumulateReport:
        return AccumulateReport(
            values=list(values),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
