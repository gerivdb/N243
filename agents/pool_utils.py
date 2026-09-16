#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pool_utils.py — N243 Pool Utils

Rôle :
- Fournir un outil de pool simple
- Publier un rapport de pool
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class PoolReport:
    pooled: List[str]
    timestamp: str


class PoolUtils:
    @staticmethod
    def inspect(pools: List[str], payload: Dict[str, Any]) -> PoolReport:
        pooled = [pool for pool in pools if payload.get(pool) is True]
        return PoolReport(
            pooled=pooled,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
