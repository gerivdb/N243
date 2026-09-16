#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
poller_utils.py — N243 Poller Utils

Rôle :
- Fournir un sondage simple avec limite et intervalle
- Exécuter une fonction jusqu'à obtenir un résultat non-None
- Publier un rapport de sondage
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Optional


@dataclass
class PollerReport:
    func_name: str
    result: Any
    attempts: int
    success: bool
    timestamp: str


class PollerUtils:
    @staticmethod
    def poll(func: Callable[[], Any], timeout: float = 10.0, interval: float = 0.5) -> Any:
        deadline = time.monotonic() + timeout
        last_result = None
        while True:
            last_result = func()
            if last_result is not None:
                return last_result
            if time.monotonic() >= deadline:
                break
            time.sleep(interval)
        return last_result

    @staticmethod
    def report(func_name: str, result: Any, attempts: int, success: bool) -> PollerReport:
        return PollerReport(
            func_name=func_name,
            result=result,
            attempts=attempts,
            success=success,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
