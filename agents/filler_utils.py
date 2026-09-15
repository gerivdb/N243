#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
filler_utils.py — N243 Filler Utils

Rôle :
- Fournir un remplisseur simple de texte
- Remplir une structure avec une valeur par défaut
- Publier un rapport de remplissage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class FillReport:
    filled: int
    timestamp: str


class FillerUtils:
    @staticmethod
    def fill_dict(data: Dict[str, Any], keys: List[str], default: Any = None) -> Dict[str, Any]:
        return {key: data.get(key, default) for key in keys}

    def report(self, filled: int) -> FillReport:
        return FillReport(
            filled=filled,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
