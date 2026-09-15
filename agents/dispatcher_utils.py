#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dispatcher_utils.py — N243 Dispatcher Utils

Rôle :
- Fournir un outil de distribution simple
- Répartir des valeurs dans des tranches
- Publier un rapport de distribution
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class DispatchReport:
    dispatched: Dict[int, List[Any]]
    timestamp: str


class DispatcherUtils:
    @staticmethod
    def distribute(values: List[Any], slots: int) -> Dict[int, List[Any]]:
        result: Dict[int, List[Any]] = {}
        for index, value in enumerate(values):
            slot = index % slots
            result.setdefault(slot, []).append(value)
        return result

    def report(self, values: List[Any], slots: int) -> DispatchReport:
        return DispatchReport(
            dispatched=self.distribute(values, slots),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
