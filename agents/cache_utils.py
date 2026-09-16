#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cache_utils.py — N24 N243 Cache Utils

Rôle :
- Fournir un outil simple de gestion de cache
- Publier un rapport de clés mises en cache
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class CacheReport:
    keys: List[str]
    timestamp: str


class CacheUtils:
    @staticmethod
    def inspect(keys: List[str]) -> CacheReport:
        return CacheReport(
            keys=list(keys),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
