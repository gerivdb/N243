#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ungroup_utils.py — N243 Ungroup Utils

Rôle :
- Fournir un dégrouper simple d'éléments
- Aplatir des groupes en une liste
- Publier un rapport de dégroupement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class UngroupReport:
    groups: int
    items: List[Any]
    timestamp: str


class UngroupUtils:
    @staticmethod
    def ungroup(groups: Dict[str, List[Any]]) -> List[Any]:
        return [item for items in groups.values() for item in items]

    def report(self, groups: Dict[str, List[Any]]) -> UngroupReport:
        return UngroupReport(
            groups=len(groups),
            items=self.ungroup(groups),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
