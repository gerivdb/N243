#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
encode_utils.py — N24 N243 Encode Utils

Rôle :
- Fournir un outil simple de gestion de codage
- Publier un rapport de formats encodés
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class EncodeReport:
    encoded: List[str]
    timestamp: str


class EncodeUtils:
    @staticmethod
    def inspect(encoded: List[str]) -> EncodeReport:
        return EncodeReport(
            encoded=list(encoded),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
