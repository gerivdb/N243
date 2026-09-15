#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
poller.py — N243 Poller

Rôle :
- Effectuer des pollings à intervalle régulier
- Collecter les résultats
- Publier un rapport de polling
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional


@dataclass
class PollResult:
    poll_name: str
    success: bool
    value: Any
    timestamp: str


class Poller:
    def __init__(self, interval_sec: float = 1.0) -> None:
        self.interval_sec = interval_sec
        self.results: List[PollResult] = []

    def poll(self, poll_name: str, operation: Callable[[], Any]) -> PollResult:
        timestamp = datetime.now(timezone.utc).isoformat()
        try:
            value = operation()
            success = True
        except Exception:
            success = False
            value = None
        result = PollResult(poll_name=poll_name, success=success, value=value, timestamp=timestamp)
        self.results.append(result)
        time.sleep(self.interval_sec)
        return result

    def report(self) -> Dict[str, Any]:
        return {
            "total": len(self.results),
            "success": sum(1 for r in self.results if r.success),
            "failure": sum(1 for r in self.results if not r.success),
            "results": [
                {
                    "poll_name": r.poll_name,
                    "success": r.success,
                    "value": r.value,
                    "timestamp": r.timestamp,
                }
                for r in self.results
            ],
        }
