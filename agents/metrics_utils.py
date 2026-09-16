#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
metrics_utils.py — N24 N243 Metrics Utils

Rôle :
- Fournir un outil simple de gestion de métriques
- Publier un rapport de métriques collectées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class MetricsReport:
    metrics: List[str]
    timestamp: str


class MetricsUtils:
    @staticmethod
    def inspect(metrics: List[str]) -> MetricsReport:
        return MetricsReport(
            metrics=list(metrics),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
