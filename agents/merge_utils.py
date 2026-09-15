#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merge_utils.py — N243 Merge Utils

Rôle :
- Fournir un outil de fusion simple
- Publier un rapport de fusion
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class MergeReport:
    merged: List[Any]
    timestamp: str


class MergeUtils:
    @staticmethod
    def apply(left: List[Any], right: List[Any]) -> MergeReport:
        merged = list(left)
        for item in right:
            if item not in merged:
                merged.append(item)
        return MergeReport(
            merged=merged,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
