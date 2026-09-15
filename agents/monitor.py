#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
monitor.py — N243 Monitor

Rôle :
- Surveiller des conditions sur des valeurs
- Publier des alertes simples
- Publier un rapport de monitoring
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional


@dataclass
class Alert:
    name: str
    condition: str
    triggered: bool
    value: Any
    timestamp: str


class Monitor:
    def __init__(self) -> None:
        self.alerts: List[Alert] = []

    def check(self, name: str, condition: str, predicate: Callable[[Any], bool], value: Any) -> Alert:
        triggered = predicate(value)
        alert = Alert(
            name=name,
            condition=condition,
            triggered=triggered,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
        self.alerts.append(alert)
        return alert

    def report(self) -> Dict[str, Any]:
        return {
            "total_checks": len(self.alerts),
            "triggered": sum(1 for a in self.alerts if a.triggered),
            "alerts": [
                {
                    "name": a.name,
                    "condition": a.condition,
                    "triggered": a.triggered,
                    "value": a.value,
                    "timestamp": a.timestamp,
                }
                for a in self.alerts
            ],
        }
