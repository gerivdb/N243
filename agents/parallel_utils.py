#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
parallel_utils.py — N243 Parallel Utils

Rôle :
- Fournir un moteur de parallélisme simple
- Distribuer des tâches sur des workers
- Collecter les résultats dans l'ordre
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, List


@dataclass
class ParallelResult:
    task_id: int
    status: str
    result: Any
    timestamp: str


class ParallelUtils:
    def run(self, tasks: List[Callable[[], Any]], max_workers: int = 2) -> List[ParallelResult]:
        results: List[ParallelResult] = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(task): index for index, task in enumerate(tasks)}
            for future in futures:
                index = futures[future]
                try:
                    value = future.result()
                    result = ParallelResult(
                        task_id=index + 1,
                        status="ok",
                        result=value,
                        timestamp=datetime.now(timezone.utc).isoformat(),
                    )
                except Exception as exc:  # noqa: BLE001
                    result = ParallelResult(
                        task_id=index + 1,
                        status="error",
                        result=None,
                        timestamp=datetime.now(timezone.utc).isoformat(),
                    )
                results.append(result)
        return results
