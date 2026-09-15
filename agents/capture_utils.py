#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
capture_utils.py — N243 Capture Utils

Rôle :
- Fournir un outil de capture simple
- Retenir les valeurs au-dessus d'un seuil
- Publier un rapport de capture
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class CaptureReport:
    captured: List[float]
    timestamp: str


class CaptureUtils:
    @staticmethod
    def above(values: List[float], threshold: float) -> CaptureReport:
        captured = [value for value in values if value > threshold]
        return CaptureReport(
            captured=captured,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
