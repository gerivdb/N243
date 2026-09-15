#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merger_utils.py — N243 Merger Utils

Rôle :
- Fournir un fusionneur simple d'objets
- Fusionner des dictionnaires
- Publier un rapport de fusion
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class MergeReport:
    sources: int
    keys: List[str]
    timestamp: str


class MergerUtils:
    @staticmethod
    def merge_dicts(left: Dict[str, Any], right: Dict[str, Any]) -> Dict[str, Any]:
        merged = dict(left)
        for key, value in right.items():
            if key in merged:
                merged[key] = value
            else:
                merged[key] = value
        return merged

    def report(self, sources: List[Dict[str, Any]]) -> MergeReport:
        keys = sorted({key for source in sources for key in source.keys()})
        return MergeReport(
            sources=len(sources),
            keys=keys,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
