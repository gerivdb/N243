#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
task_utils.py — N24 N243 Task Utils

Rôle :
- Fournir un outil de planification simple de tâches
- Publier un rapport de tâches planifiées
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List


@dataclass
class TaskReport:
    scheduled: List[str]
    timestamp: str


class TaskUtils:
    @staticmethod
    def inspect(tasks: List[str]) -> TaskReport:
        scheduled = list(tasks)
        return TaskReport(
            scheduled=scheduled,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
