#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
split_utils.py — N243 Split Utils

Rôle :
- Fournir un outil de fractionnement simple
- Publier un rapport de fractionnement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class SplitReport:
    left: List[Any]
    right: List[Any]
    timestamp: str


class SplitUtils:
    @staticmethod
    def apply(values: List[Any], index: int) -> SplitReport:
        return SplitReport(
            left=list(values[:index]),
            right=list(values[index:]),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
