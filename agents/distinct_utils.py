#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
distinct_utils.py — N243 Distinct Utils

Rôle :
- Fournir un outil de distinction simple
- Publier un rapport de distinction
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class DistinctReport:
    distinct: List[Any]
    timestamp: str


class DistinctUtils:
    @staticmethod
    def apply(values: List[Any]) -> DistinctReport:
        distinct: List[Any] = []
        for value in values:
            if value not in distinct:
                distinct.append(value)
        return DistinctReport(
            distinct=distinct,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
