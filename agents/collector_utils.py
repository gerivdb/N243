#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collector_utils.py — N243 Collector Utils

Rôle :
- Fournir un outil de collecte simple
- Publier un rapport de collecte
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class CollectorReport:
    collected: List[str]
    timestamp: str


class CollectorUtils:
    @staticmethod
    def inspect(items: List[str], payload: Dict[str, Any]) -> CollectorReport:
        collected = [item for item in items if payload.get(item) is True]
        return CollectorReport(
            collected=collected,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
