#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
metrics_utils.py — N243 Metrics Utils

Rôle :
- Fournir un outil de métriques simple
- Publier un rapport de métriques
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class MetricsReport:
    collected: List[str]
    timestamp: str


class MetricsUtils:
    @staticmethod
    def collect(metrics: List[str], payload: Dict[str, Any]) -> MetricsReport:
        collected = [metric for metric in metrics if payload.get(metric) is not None]
        return MetricsReport(
            collected=collected,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
