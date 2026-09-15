#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
loader_utils.py — N243 Loader Utils

Rôle :
- Fournir un outil de chargement simple
- Publier un rapport de chargement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class LoaderReport:
    loaded: List[str]
    timestamp: str


class LoaderUtils:
    @staticmethod
    def inspect(sources: List[str], payload: Dict[str, Any]) -> LoaderReport:
        loaded = [source for source in sources if payload.get(source) is True]
        return LoaderReport(
            loaded=loaded,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
