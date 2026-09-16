#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
round_utils.py — N243 Round Utils

Rôle :
- Fournir des utilitaires d'arrondi
- Round half up, floor, ceil
- Publier un rapport d'arrondi
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP


@dataclass
class RoundReport:
    operation: str
    value: float
    timestamp: str


class RoundUtils:
    @staticmethod
    def round_half_up(value: float, ndigits: int = 0) -> float:
        quantize_str = "0." + "0" * ndigits if ndigits > 0 else "1"
        return float(Decimal(str(value)).quantize(Decimal(quantize_str), rounding=ROUND_HALF_UP))

    @staticmethod
    def floor(value: float, ndigits: int = 0) -> float:
        factor = 10**ndigits
        return float(int(value * factor) / factor)

    @staticmethod
    def ceil(value: float, ndigits: int = 0) -> float:
        factor = 10**ndigits
        return float(math.ceil(value * factor) / factor)

    @staticmethod
    def report(operation: str, value: float) -> RoundReport:
        return RoundReport(
            operation=operation,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
