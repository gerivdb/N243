#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
padder_utils.py — N243 Padder Utils

Rôle :
- Fournir un rembourreur simple de texte
- Ajouter du padding à gauche ou à droite
- Publier un rapport de rembourrage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class PadReport:
    original_length: int
    padded_length: int
    timestamp: str


class PadderUtils:
    @staticmethod
    def pad(value: str, width: int, char: str = " ", align: str = "left") -> str:
        if align == "right":
            return value.rjust(width, char)
        return value.ljust(width, char)

    def report(self, original: str, padded: str) -> PadReport:
        return PadReport(
            original_length=len(original),
            padded_length=len(padded),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
