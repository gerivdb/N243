#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
encoder_utils.py — N243 Encoder Utils

Rôle :
- Fournir un encodeur simple de texte
- Encoder en base64
- Publier un rapport d'encodage
"""

from __future__ import annotations

import base64
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class EncodeReport:
    original_length: int
    encoded_length: int
    timestamp: str


class EncoderUtils:
    @staticmethod
    def encode_base64(value: str) -> str:
        return base64.b64encode(value.encode("utf-8")).decode("utf-8")

    def report(self, original: str, encoded: str) -> EncodeReport:
        return EncodeReport(
            original_length=len(original),
            encoded_length=len(encoded),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
