#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
concurrency_utils.py — N243 Concurrency Utils

Rôle :
- Fournir un moteur de workers simple et borné
- Distribuer des tâches, collecter les résultats
- Publier un rapport d'exécution
"""

from __future__ import annotations

import queue
import threading
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass
class TaskResult:
    task_id: str
    status: str
    result: Any
    error: Optional[str]
    timestamp: str


class ConcurrencyUtils:
    def run_tasks(self, tasks: List[Callable[[], Any]], max_workers: int = 2) -> List[TaskResult]:
        q: queue.SimpleQueue = queue.SimpleQueue()
        results: List[TaskResult] = []
        lock = threading.Lock()

        def worker(task_id: str, func: Callable[[], Any]) -> None:
            try:
                value = func()
                result = TaskResult(
                    task_id=task_id,
                    status="ok",
                    result=value,
                    error=None,
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
            except Exception as exc:  # noqa: BLE001
                result = TaskResult(
                    task_id=task_id,
                    status="error",
                    result=None,
                    error=str(exc),
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
            with lock:
                results.append(result)

        threads = []
        for index, func in enumerate(tasks[:max_workers]):
            task_id = f"task-{index + 1}"
            thread = threading.Thread(target=worker, args=(task_id, func))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return results
