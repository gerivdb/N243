#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
expander_utils.py — N243 Expander Utils

Rôle :
- Fournir un expanseur simple de valeurs
- Étendre des listes ou des chaînes
- Publier un rapport d'expansion
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class ExpandReport:
    original: Any
    expanded: List[Any]
    timestamp: str


class ExpanderUtils:
    @staticmethod
    def expand_list(values: List[Any], repeat: int = 1) -> List[Any]:
        return [item for value in values for item in [value] * repeat]

    def report(self, original: Any, expanded: List[Any]) -> ExpandReport:
        return ExpandReport(
            original=original,
            expanded=expanded,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
