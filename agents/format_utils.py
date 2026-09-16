#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
format_utils.py — N24 N243 Format Utils

Rôle :
- Fournir un outil simple de gestion de formats
- Publier un rapport de formats détectés
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class FormatReport:
    formats: List[str]
    timestamp: str


class FormatUtils:
    @staticmethod
    def inspect(formats: List[str]) -> FormatReport:
        return FormatReport(
            formats=list(formats),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
