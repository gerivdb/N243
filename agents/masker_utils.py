#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
masker_utils.py — N243 Masker Utils

Rôle :
- Fournir un masqueur simple de texte
- Remplacer des caractères par un masque
- Publier un rapport de masquage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class MaskReport:
    original_length: int
    masked_length: int
    timestamp: str


class MaskerUtils:
    @staticmethod
    def mask(value: str, mask_char: str = "*", visible: int = 0) -> str:
        if len(value) <= visible:
            return value
        return value[:visible] + mask_char * (len(value) - visible)

    def report(self, original: str, masked: str) -> MaskReport:
        return MaskReport(
            original_length=len(original),
            masked_length=len(masked),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
