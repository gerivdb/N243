#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scheduler_utils.py — N243 Scheduler Utils

Rôle :
- Fournir un outil de planification simple
- Publier un rapport de planification
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class SchedulerReport:
    scheduled: List[str]
    timestamp: str


class SchedulerUtils:
    @staticmethod
    def inspect(jobs: List[str], payload: Dict[str, Any]) -> SchedulerReport:
        scheduled = [job for job in jobs if payload.get(job) is True]
        return SchedulerReport(
            scheduled=scheduled,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
