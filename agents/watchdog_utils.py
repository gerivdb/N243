#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
watchdog_utils.py — N243 Watchdog Utils

Rôle :
- Fournir un outil de surveillance simple
- Publier un rapport de surveillance
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class WatchdogReport:
    alive: int
    timestamp: str


class WatchdogUtils:
    @staticmethod
    def check(payloads: List[Dict[str, Any]]) -> WatchdogReport:
        alive = sum(1 for payload in payloads if payload.get("alive", False))
        return WatchdogReport(
            alive=alive,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
