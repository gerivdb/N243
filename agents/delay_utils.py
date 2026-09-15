#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
delay_utils.py — N243 Delay Utils

Rôle :
- Fournir un outil de temporisation simple
- Reporter une exécution d'un nombre de cycles
- Publier un rapport de temporisation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class DelayReport:
    delayed: List[Any]
    cycles: int
    timestamp: str


class DelayUtils:
    @staticmethod
    def defer(values: List[Any], cycles: int) -> DelayReport:
        return DelayReport(
            delayed=values,
            cycles=cycles,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
