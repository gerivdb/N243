#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
metric_aggregator.py — N243 Metric Aggregator

Rôle :
- Agréger des métriques provenant de plusieurs sources
- Calculer des moyennes, sommes, min, max
- Publier un rapport agrégé
"""

from __future__ import annotations

import json
import statistics
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class MetricSample:
    source: str
    name: str
    value: float
    timestamp: str


class MetricAggregator:
    def __init__(self) -> None:
        self.samples: List[MetricSample] = []

    def add_sample(self, sample: MetricSample) -> None:
        self.samples.append(sample)

    def aggregate_by_name(self, metric_name: str) -> Dict[str, Any]:
        values = [s.value for s in self.samples if s.name == metric_name]
        if not values:
            return {
                "name": metric_name,
                "count": 0,
                "avg": 0.0,
                "min": 0.0,
                "max": 0.0,
                "median": 0.0,
            }
        return {
            "name": metric_name,
            "count": len(values),
            "avg": statistics.mean(values),
            "min": min(values),
            "max": max(values),
            "median": statistics.median(values),
        }

    def aggregate_all(self) -> List[Dict[str, Any]]:
        names = sorted({s.name for s in self.samples})
        return [self.aggregate_by_name(name) for name in names]

    def to_json(self) -> str:
        return json.dumps(self.aggregate_all(), ensure_ascii=False, indent=2)
