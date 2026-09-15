#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decompressor_utils.py — N243 Decompressor Utils

Rôle :
- Fournir un décompresseur simple de texte
- Restaurer des espaces compressés
- Publier un rapport de décompression
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class DecompressReport:
    original_length: int
    decompressed_length: int
    timestamp: str


class DecompressorUtils:
    @staticmethod
    def decompress(value: str, placeholder: str = " ") -> str:
        return value.replace(placeholder, "    ")

    def report(self, original: str, decompressed: str) -> DecompressReport:
        return DecompressReport(
            original_length=len(original),
            decompressed_length=len(decompressed),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
