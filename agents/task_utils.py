#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
task_utils.py — N243 Task Utils

Rôle :
- Fournir un gestionnaire de tâches simple
- Publier un rapport de tâches
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class TaskReport:
    completed: List[str]
    timestamp: str


class TaskUtils:
    @staticmethod
    def complete(tasks: List[str], payload: Dict[str, Any]) -> TaskReport:
        completed = [task for task in tasks if payload.get(task) is True]
        return TaskReport(
            completed=completed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
