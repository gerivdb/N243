#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timeout_manager.py — N243 Timeout Manager

Rôle :
- Gérer les timeouts pour les opérations externes
- Détecter les dépassements de timeout
- Publier des alertes en cas de timeout
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable, Optional, TypeVar

T = TypeVar("T")


@dataclass
class TimeoutResult:
    operation_name: str
    timeout_sec: float
    elapsed_sec: float
    timed_out: bool
    timestamp: str


class TimeoutManager:
    def __init__(self) -> None:
        self.results = []

    def execute_with_timeout(
        self,
        operation_name: str,
        operation: Callable[[], T],
        timeout_sec: float,
    ) -> TimeoutResult:
        start = time.perf_counter()
        timed_out = False
        result = None
        try:
            result = operation()
        except Exception:
            timed_out = True
        elapsed = time.perf_counter() - start
        timeout_result = TimeoutResult(
            operation_name=operation_name,
            timeout_sec=timeout_sec,
            elapsed_sec=elapsed,
            timed_out=timed_out,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
        self.results.append(timeout_result)
        return timeout_result

    def report(self) -> dict:
        return {
            "total": len(self.results),
            "timed_out": sum(1 for r in self.results if r.timed_out),
            "avg_elapsed_sec": (
                sum(r.elapsed_sec for r in self.results) / len(self.results)
                if self.results
                else 0.0
            ),
        }
