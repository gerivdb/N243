#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
executor_utils.py — N243 Executor Utils

Rôle :
- Fournir un exécuteur simple d'actions enchaînées
- Exécuter une chaîne de steps, ou jusqu'à un prédicat
- Publier un rapport d'exécution
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, List


@dataclass
class ExecutorReport:
    stopped_by_predicate: bool
    executed: List[Any] = field(default_factory=list)
    timestamp: str = ""


class ExecutorUtils:
    @staticmethod
    def execute_chain(steps: List[Callable[[], Any]]) -> List[Any]:
        results: List[Any] = []
        for step in steps:
            results.append(step())
        return results

    @staticmethod
    def execute_until(predicate: Callable[[Any], bool], steps: List[Callable[[], Any]]) -> List[Any]:
        results: List[Any] = []
        for step in steps:
            value = step()
            results.append(value)
            if predicate(value):
                break
        return results

    @staticmethod
    def report(steps: List[Callable[[], Any]], stop: bool = False) -> ExecutorReport:
        return ExecutorReport(
            executed=[],
            stopped_by_predicate=stop,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
