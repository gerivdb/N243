#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cycle_stats_collector.py — N243 Cycle Stats Collector

Rôle :
- Collecter des statistiques simples sur les cycles N243
- Calculer les moyennes, min, max, médianes
- Publier un rapport agrégé
"""

from __future__ import annotations

import json
import statistics
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class CycleRecord:
    cycle_id: str
    duration_sec: float
    events_success: int
    events_total: int
    curx_score: float
    timestamp: str


class CycleStatsCollector:
    def __init__(self) -> None:
        self.cycles: List[CycleRecord] = []

    def add_cycle(self, record: CycleRecord) -> None:
        self.cycles.append(record)

    def summary(self) -> Dict[str, Any]:
        if not self.cycles:
            return {
                "count": 0,
                "avg_duration_sec": 0.0,
                "min_duration_sec": 0.0,
                "max_duration_sec": 0.0,
                "median_duration_sec": 0.0,
                "avg_success_rate": 0.0,
                "avg_curx_score": 0.0,
            }
        durations = [c.duration_sec for c in self.cycles]
        success_rates = [
            c.events_success / c.events_total if c.events_total > 0 else 0.0
            for c in self.cycles
        ]
        curx_scores = [c.curx_score for c in self.cycles]
        return {
            "count": len(self.cycles),
            "avg_duration_sec": statistics.mean(durations),
            "min_duration_sec": min(durations),
            "max_duration_sec": max(durations),
            "median_duration_sec": statistics.median(durations),
            "avg_success_rate": statistics.mean(success_rates),
            "avg_curx_score": statistics.mean(curx_scores),
        }

    def to_json(self) -> str:
        return json.dumps(self.summary(), ensure_ascii=False, indent=2)
