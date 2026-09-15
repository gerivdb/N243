#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scheduler_utils.py — N243 Scheduler Utils

Rôle :
- Fournir un ordonnanceur de tâches simple
- Planifier, exécuter, annuler des tâches
- Publier un rapport d'exécution
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional


@dataclass
class ScheduledTask:
    name: str
    func: Callable[[], Any]
    executed: bool
    result: Any
    timestamp: str


class SchedulerUtils:
    def __init__(self) -> None:
        self._tasks: Dict[str, ScheduledTask] = {}

    def schedule(self, name: str, func: Callable[[], Any]) -> None:
        self._tasks[name] = ScheduledTask(
            name=name,
            func=func,
            executed=False,
            result=None,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def run(self, name: str) -> Any:
        task = self._tasks.get(name)
        if task is None:
            raise KeyError(name)
        task.executed = True
        task.result = task.func()
        return task.result

    def cancel(self, name: str) -> None:
        self._tasks.pop(name, None)

    def report(self, name: str) -> Optional[ScheduledTask]:
        return self._tasks.get(name)
