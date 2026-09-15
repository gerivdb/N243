#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
spectrum_utils.py — N243 Spectrum Utils

Rôle :
- Fournir un outil de spectre simple
- Calculer les amplitudes d'une série
- Publier un rapport de spectre
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class SpectrumReport:
    max_amplitude: float
    timestamp: str


class SpectrumUtils:
    @staticmethod
    def amplitudes(values: List[float]) -> List[float]:
        return [abs(value) for value in values]

    def report(self, values: List[float]) -> SpectrumReport:
        return SpectrumReport(
            max_amplitude=max(self.amplitudes(values)) if values else 0.0,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
