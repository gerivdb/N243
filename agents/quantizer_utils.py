#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
quantizer_utils.py — N243 Quantizer Utils

Rôle :
- Fournir un outil de quantification simple
- Réduire la précision de valeurs flottantes
- Publier un rapport de quantification
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class QuantizeReport:
    original: List[float]
    quantized: List[float]
    timestamp: str


class QuantizerUtils:
    @staticmethod
    def quantize(values: List[float], precision: int = 2) -> List[float]:
        return [round(value, precision) for value in values]

    def report(self, values: List[float], precision: int = 2) -> QuantizeReport:
        return QuantizeReport(
            original=values,
            quantized=self.quantize(values, precision),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
