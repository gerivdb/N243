#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
parse_utils.py — N24 N243 Parse Utils

Rôle :
- Fournir un outil simple de parsing
- Publier un rapport de données parsées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ParseReport:
    parsed: List[str]
    timestamp: str


class ParseUtils:
    @staticmethod
    def inspect(parsed: List[str]) -> ParseReport:
        return ParseReport(
            parsed=list(parsed),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
