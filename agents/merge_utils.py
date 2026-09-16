#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merge_utils.py — N24 N243 Merge Utils

Rôle :
- Fournir un outil simple de fusion
- Publier un rapport de fusions effectuées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class MergeReport:
    merges: List[str]
    timestamp: str


class MergeUtils:
    @staticmethod
    def inspect(merges: List[str]) -> MergeReport:
        return MergeReport(
            merges=list(merges),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
