#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decoder_utils.py — N243 Decoder Utils

Rôle :
- Fournir un décodeur simple de texte
- Décoder du base64
- Publier un rapport de décodage
"""

from __future__ import annotations

import base64
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class DecodeReport:
    original_length: int
    decoded_length: int
    timestamp: str


class DecoderUtils:
    @staticmethod
    def decode_base64(value: str) -> str:
        return base64.b64decode(value.encode("utf-8")).decode("utf-8")

    def report(self, original: str, decoded: str) -> DecodeReport:
        return DecodeReport(
            original_length=len(original),
            decoded_length=len(decoded),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
