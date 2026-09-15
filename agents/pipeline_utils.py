#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pipeline_utils.py — N243 Pipeline Utils

Rôle :
- Fournir un pipeline d'étapes simple
- Chaîner des fonctions, récupérer le résultat final
- Publier un rapport par étape
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, List


@dataclass
class StepReport:
    step: int
    status: str
    input: Any
    output: Any
    timestamp: str


class PipelineUtils:
    def __init__(self, steps: List[Callable[[Any], Any]]) -> None:
        self._steps = steps

    def run(self, value: Any) -> Any:
        current = value
        for index, step in enumerate(self._steps, start=1):
            input_value = current
            current = step(current)
        return current

    def run_with_reports(self, value: Any) -> tuple[Any, List[StepReport]]:
        current = value
        reports: List[StepReport] = []
        for index, step in enumerate(self._steps, start=1):
            input_value = current
            current = step(current)
            reports.append(
                StepReport(
                    step=index,
                    status="ok",
                    input=input_value,
                    output=current,
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
            )
        return current, reports
