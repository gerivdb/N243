#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compressor_utils.py — N243 Compressor Utils

Rôle :
- Fournir un compresseur simple de texte
- Supprimer les espaces multiples
- Publier un rapport de compression
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class CompressReport:
    original_length: int
    compressed_length: int
    timestamp: str


class CompressorUtils:
    @staticmethod
    def compress(value: str) -> str:
        return re.sub(r"\s+", " ", value).strip()

    def report(self, original: str, compressed: str) -> CompressReport:
        return CompressReport(
            original_length=len(original),
            compressed_length=len(compressed),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
