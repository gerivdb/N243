#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decode_utils.py — N24 N243 Decode Utils

Rôle :
- Fournir un outil simple de décodage
- Publier un rapport de formats décodés
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class DecodeReport:
    decoded: List[str]
    timestamp: str


class DecodeUtils:
    @staticmethod
    def inspect(decoded: List[str]) -> DecodeReport:
        return DecodeReport(
            decoded=list(decoded),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
