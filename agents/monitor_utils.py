#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
monitor_utils.py — N243 Monitor Utils

Rôle :
- Fournir un outil de监控 simple
- Publier un rapport de监控
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class MonitorReport:
    monitored: List[str]
    timestamp: str


class MonitorUtils:
    @staticmethod
    def watch(metrics: List[str], payload: Dict[str, Any]) -> MonitorReport:
        monitored = [metric for metric in metrics if payload.get(metric) is not None]
        return MonitorReport(
            monitored=monitored,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
