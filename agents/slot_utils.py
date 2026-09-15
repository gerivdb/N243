#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
slot_utils.py — N243 Slot Utils

Rôle :
- Fournir un outil de tranche simple
- Sélectionner une sous-liste par plage
- Publier un rapport de tranche
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class SlotReport:
    slot: List[Any]
    timestamp: str


class SlotUtils:
    @staticmethod
    def range(values: List[Any], start: int, end: int) -> SlotReport:
        return SlotReport(
            slot=values[start:end],
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
