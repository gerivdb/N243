#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
trim_utils.py — N243 Trim Utils

Rôle :
- Fournir un outil d'élagage simple
- Publier un rapport d'élagage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class TrimReport:
    trimmed: List[Any]
    timestamp: str


class TrimUtils:
    @staticmethod
    def apply(values: List[Any], width: int) -> TrimReport:
        return TrimReport(
            trimmed=list(values[:width]),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
