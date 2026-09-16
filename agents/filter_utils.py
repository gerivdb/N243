#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
filter_utils.py — N24 N243 Filter Utils

Rôle :
- Fournir un outil simple de filtrage
- Publier un rapport de filtres appliqués
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class FilterReport:
    filters: List[str]
    timestamp: str


class FilterUtils:
    @staticmethod
    def inspect(filters: List[str]) -> FilterReport:
        return FilterReport(
            filters=list(filters),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
