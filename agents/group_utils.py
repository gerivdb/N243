#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
group_utils.py — N243 Group Utils

Rôle :
- Fournir un groupeur simple d'éléments
- Grouper par clé avec agrégation de listes
- Publier un rapport de groupement
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class GroupReport:
    groups: int
    keys: List[str]
    timestamp: str


class GroupUtils:
    @staticmethod
    def group_by_key(items: List[Dict[str, Any]], key: str) -> Dict[str, List[Any]]:
        grouped: Dict[str, List[Any]] = defaultdict(list)
        for item in items:
            grouped[item[key]].append(item)
        return dict(grouped)

    def report(self, groups: Dict[str, List[Any]]) -> GroupReport:
        return GroupReport(
            groups=len(groups),
            keys=list(groups.keys()),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
