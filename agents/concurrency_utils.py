#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
concurrency_utils.py — N24 N243 Concurrency Utils

Rôle :
- Fournir un outil simple de gestion de concurrence
- Publier un rapport de tâches concurrentes traitées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ConcurrencyReport:
    tasks: List[str]
    timestamp: str


class ConcurrencyUtils:
    @staticmethod
    def inspect(tasks: List[str]) -> ConcurrencyReport:
        return ConcurrencyReport(
            tasks=list(tasks),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
