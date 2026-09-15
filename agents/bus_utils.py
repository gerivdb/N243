#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bus_utils.py — N243 Bus Utils

Rôle :
- Fournir un outil de bus simple
- Publier un rapport de bus
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class BusReport:
    routed: List[str]
    timestamp: str


class BusUtils:
    @staticmethod
    def inspect(buses: List[str], payload: Dict[str, Any]) -> BusReport:
        routed = [bus for bus in buses if payload.get(bus) is True]
        return BusReport(
            routed=routed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
