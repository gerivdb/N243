#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert_utils.py — N24 N243 Convert Utils

Rôle :
- Fournir un outil simple de conversion
- Publier un rapport de conversions effectuées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ConvertReport:
    conversions: List[str]
    timestamp: str


class ConvertUtils:
    @staticmethod
    def inspect(conversions: List[str]) -> ConvertReport:
        return ConvertReport(
            conversions=list(conversions),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
