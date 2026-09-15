#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timer.py — N243 Timer

Rôle :
- Mesurer des durées d'opérations
- Enregistrer des points de repère
- Publier un rapport de chronométrage
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, List, Optional


@dataclass
class Benchmark:
    name: str
    elapsed_sec: float
    timestamp: str


class Timer:
    def __init__(self) -> None:
        self.start_time: float = time.perf_counter()
        self.benchmarks: List[Benchmark] = []

    def mark(self, name: str) -> Benchmark:
        elapsed = time.perf_counter() - self.start_time
        benchmark = Benchmark(
            name=name,
            elapsed_sec=elapsed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
        self.benchmarks.append(benchmark)
        return benchmark

    def report(self) -> Dict[str, Any]:
        return {
            "total_marks": len(self.benchmarks),
            "last_elapsed_sec": self.benchmarks[-1].elapsed_sec if self.benchmarks else 0.0,
            "benchmarks": [
                {
                    "name": b.name,
                    "elapsed_sec": b.elapsed_sec,
                    "timestamp": b.timestamp,
                }
                for b in self.benchmarks
            ],
        }
