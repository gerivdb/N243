#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decomposer_utils.py — N243 Decomposer Utils

Rôle :
- Fournir un décomposeur simple d'éléments
- Séparer une chaîne en éléments
- Publier un rapport de décomposition
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class DecomposeReport:
    count: int
    timestamp: str


class DecomposerUtils:
    @staticmethod
    def decompose(value: str, separator: str = ", ") -> List[str]:
        return [item.strip() for item in value.split(separator) if item.strip()]

    def report(self, items: List[str]) -> DecomposeReport:
        return DecomposeReport(
            count=len(items),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
