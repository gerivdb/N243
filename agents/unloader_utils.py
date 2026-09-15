#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unloader_utils.py — N243 Unloader Utils

Rôle :
- Fournir un déchargeur simple de données
- Extraire des éléments depuis une source
- Publier un rapport de déchargement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class UnloadReport:
    source: str
    unloaded: int
    timestamp: str


class UnloaderUtils:
    @staticmethod
    def unload_keys(source: Dict[str, Any]) -> List[str]:
        return list(source.keys())

    @staticmethod
    def unload_values(source: Dict[str, Any]) -> List[Any]:
        return list(source.values())

    def report(self, source: str, unloaded: int) -> UnloadReport:
        return UnloadReport(
            source=source,
            unloaded=unloaded,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
