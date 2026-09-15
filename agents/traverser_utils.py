#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
traverser_utils.py — N243 Traverser Utils

Rôle :
- Fournir un parcoureur simple de structure
- Parcourir en profondeur un dictionnaire
- Publier un rapport de parcours
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Tuple


@dataclass
class TraverseReport:
    paths: List[str]
    timestamp: str


class TraverserUtils:
    @staticmethod
    def traverse(data: Dict[str, Any], prefix: str = "") -> List[Tuple[str, Any]]:
        results: List[Tuple[str, Any]] = []
        for key, value in data.items():
            path = f"{prefix}.{key}" if prefix else key
            results.append((path, value))
            if isinstance(value, dict):
                results.extend(TraverserUtils.traverse(value, prefix=path))
        return results

    def report(self, paths: List[Tuple[str, Any]]) -> TraverseReport:
        return TraverseReport(
            paths=[path for path, _ in paths],
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
