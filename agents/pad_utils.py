#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pad_utils.py — N243 Pad Utils

Rôle :
- Fournir un outil de remplissage simple
- Publier un rapport de remplissage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class PadReport:
    padded: List[Any]
    timestamp: str


class PadUtils:
    @staticmethod
    def apply(values: List[Any], width: int, fill: Any = None) -> PadReport:
        padded = list(values)
        while len(padded) < width:
            padded.append(fill)
        return PadReport(
            padded=padded,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
