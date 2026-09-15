#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
loader_utils.py — N243 Loader Utils

Rôle :
- Fournir un chargeur simple de données
- Charger depuis un dictionnaire ou une source
- Publier un rapport de chargement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class LoaderReport:
    source: str
    loaded: int
    timestamp: str


class LoaderUtils:
    @staticmethod
    def load_from_dict(source: Dict[str, Any], default: Any = None) -> Dict[str, Any]:
        return dict(source)

    def load_items(self, source: Dict[str, Any]) -> List[Any]:
        return list(source.values())

    def report(self, source: str, loaded: int) -> LoaderReport:
        return LoaderReport(
            source=source,
            loaded=loaded,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
