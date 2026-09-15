#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
worker_utils.py — N243 Worker Utils

Rôle :
- Fournir un worker simple exécutant des tâches
- Traiter une file de tâches
- Publier un rapport par tâche
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, List, Optional


@dataclass
class WorkerResult:
    task_id: int
    status: str
    result: Any
    error: Optional[str]
    timestamp: str


class WorkerUtils:
    def __init__(self, handler: Callable[[Any], Any]) -> None:
        self._handler = handler

    def process(self, tasks: List[Any]) -> List[WorkerResult]:
        results: List[WorkerResult] = []
        for index, task in enumerate(tasks, start=1):
            try:
                value = self._handler(task)
                result = WorkerResult(
                    task_id=index,
                    status="ok",
                    result=value,
                    error=None,
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
            except Exception as exc:  # noqa: BLE001
                result = WorkerResult(
                    task_id=index,
                    status="error",
                    result=None,
                    error=str(exc),
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
            results.append(result)
        return results
