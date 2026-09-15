#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
trimmer_utils.py — N243 Trimmer Utils

Rôle :
- Fournir un rogneur simple de texte
- Tronquer à une longueur maximale
- Publier un rapport de rognage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class TrimReport:
    original_length: int
    trimmed_length: int
    timestamp: str


class TrimmerUtils:
    @staticmethod
    def trim(value: str, max_length: int, suffix: str = "...") -> str:
        if len(value) <= max_length:
            return value
        return value[:max_length - len(suffix)] + suffix

    def report(self, original: str, trimmed: str) -> TrimReport:
        return TrimReport(
            original_length=len(original),
            trimmed_length=len(trimmed),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
