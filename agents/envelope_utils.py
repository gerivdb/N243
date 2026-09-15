#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
envelope_utils.py — N243 Envelope Utils

Rôle :
- Fournir un outil d'enveloppe simple
- Calculer l'enveloppe supérieure/inférieure d'une série
- Publier un rapport d'enveloppe
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class EnvelopeReport:
    upper: float
    lower: float
    timestamp: str


class EnvelopeUtils:
    @staticmethod
    def bounds(values: List[float]) -> EnvelopeReport:
        if not values:
            return EnvelopeReport(upper=0.0, lower=0.0, timestamp=datetime.now(timezone.utc).isoformat())
        return EnvelopeReport(
            upper=max(values),
            lower=min(values),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
