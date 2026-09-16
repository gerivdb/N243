#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bus_utils.py — N24 N243 Bus Utils

Rôle :
- Fournir un outil simple de gestion de bus
- Publier un rapport de messages de bus traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class BusReport:
    messages: List[str]
    timestamp: str


class BusUtils:
    @staticmethod
    def inspect(messages: List[str]) -> BusReport:
        return BusReport(
            messages=list(messages),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
