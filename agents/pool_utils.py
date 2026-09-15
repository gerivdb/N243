#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pool_utils.py — N243 Pool Utils

Rôle :
- Fournir un outil de pool simple
- Regrouper des valeurs
- Publier un rapport de pool
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class PoolReport:
    groups: int
    timestamp: str


class PoolUtils:
    @staticmethod
    def group(values: List[Any], key: str) -> Dict[Any, List[Any]]:
        groups: Dict[Any, List[Any]] = {}
        for value in values:
            groups.setdefault(value, []).append(value)
        return groups

    def report(self, values: List[Any]) -> PoolReport:
        groups = self.group(values, key="self")
        return PoolReport(
            groups=len(groups),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
