#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merger_utils.py — N243 Merger Utils

Rôle :
- Fournir un fusionneur simple pour des dictionnaires
- Fusionner des mappings en profondeur
- Publier un rapport de fusion
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class MergeResult:
    sources: int
    keys_added: int
    keys_overwritten: int
    timestamp: str


class MergerUtils:
    @staticmethod
    def merge(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        result = dict(base)
        keys_added = 0
        keys_overwritten = 0
        for key, value in override.items():
            if key in result:
                keys_overwritten += 1
            else:
                keys_added += 1
            result[key] = value
        return result

    def report(self, base: Dict[str, Any], override: Dict[str, Any]) -> MergeResult:
        merged = self.merge(base, override)
        keys_added = sum(1 for key in override if key not in base)
        keys_overwritten = sum(1 for key in override if key in base)
        return MergeResult(
            sources=2,
            keys_added=keys_added,
            keys_overwritten=keys_overwritten,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
