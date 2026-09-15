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
    messages: int
    timestamp: str


class BusUtils:
    @staticmethod
    def publish(values: List[Dict[str, Any]]) -> BusReport:
        return BusReport(
            messages=len(values),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
