#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sequencer.py — N243 Sequencer

Rôle :
- Séquence des étapes de traitement
- Exécuter les étapes dans l'ordre
- Publier un rapport de séquence
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional


@dataclass
class StepResult:
    step_name: str
    success: bool
    result: Any
    timestamp: str


class Sequencer:
    def __init__(self) -> None:
        self.results: List[StepResult] = []

    def run_step(self, name: str, operation: Callable[[], Any]) -> StepResult:
        timestamp = datetime.now(timezone.utc).isoformat()
        try:
            result = operation()
            success = True
        except Exception as e:
            result = str(e)
            success = False
        step_result = StepResult(step_name=name, success=success, result=result, timestamp=timestamp)
        self.results.append(step_result)
        return step_result

    def run_sequence(self, steps: List[tuple[str, Callable[[], Any]]]) -> List[StepResult]:
        results = []
        for name, operation in steps:
            results.append(self.run_step(name, operation))
        return results

    def report(self) -> Dict[str, Any]:
        return {
            "total_steps": len(self.results),
            "success": sum(1 for r in self.results if r.success),
            "failure": sum(1 for r in self.results if not r.success),
            "results": [
                {
                    "step_name": r.step_name,
                    "success": r.success,
                    "result": r.result,
                    "timestamp": r.timestamp,
                }
                for r in self.results
            ],
        }
