#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
clip_utils.py — N243 Clip Utils

Rôle :
- Fournir un outil de découpage par seuil simple
- Publier un rapport de découpage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ClipReport:
    clipped: List[Any]
    timestamp: str


class ClipUtils:
    @staticmethod
    def apply(values: List[Any], minimum: Any, maximum: Any) -> ClipReport:
        clipped = [min(maximum, max(minimum, value)) for value in values]
        return ClipReport(
            clipped=clipped,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
