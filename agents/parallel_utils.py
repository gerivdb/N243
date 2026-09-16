#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
parallel_utils.py — N24 N243 Parallel Utils

Rôle :
- Fournir un outil simple de gestion de parallélisme
- Publier un rapport de tâches parallélisées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ParallelReport:
    parallel: List[str]
    timestamp: str


class ParallelUtils:
    @staticmethod
    def inspect(parallel: List[str]) -> ParallelReport:
        return ParallelReport(
            parallel=list(parallel),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
