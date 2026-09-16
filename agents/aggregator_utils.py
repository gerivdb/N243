#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aggregator_utils.py — N243 Aggregator Utils

Rôle :
- Fournir un outil d’agrégation simple
- Publier un rapport d’agrégation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class AggregatorReport:
    aggregated: List[str]
    timestamp: str


class AggregatorUtils:
    @staticmethod
    def inspect(items: List[str], payload: Dict[str, Any]) -> AggregatorReport:
        aggregated = [item for item in items if payload.get(item) is True]
        return AggregatorReport(
            aggregated=aggregated,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
