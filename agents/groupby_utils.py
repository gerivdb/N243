#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
groupby_utils.py — N243 GroupBy Utils

Rôle :
- Fournir un outil de regroupement simple
- Publier un rapport de regroupement
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass
class GroupByReport:
    groups: Dict[str, List[Any]]
    timestamp: str


class GroupByUtils:
    @staticmethod
    def apply(values: List[Any], key: Callable[[Any], str]) -> GroupByReport:
        groups: Dict[str, List[Any]] = defaultdict(list)
        for value in values:
            groups[key(value)].append(value)
        return GroupByReport(
            groups=dict(groups),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
