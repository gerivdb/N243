#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
shaper_utils.py — N243 Shaper Utils

Rôle :
- Fournir un formeur simple d'objets
- Transformer des données selon un moule
- Publier un rapport de formage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class ShapeReport:
    shaped: int
    timestamp: str


class ShaperUtils:
    @staticmethod
    def shape(data: Dict[str, Any], mold: Dict[str, Any]) -> Dict[str, Any]:
        return {key: mold.get(key, value) for key, value in data.items()}

    def report(self, shaped: int) -> ShapeReport:
        return ShapeReport(
            shaped=shaped,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
