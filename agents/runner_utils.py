#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
runner_utils.py — N243 Runner Utils

Rôle :
- Fournir un exécuteur d’étapes simple
- Publier un rapport d’exécution
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class RunnerReport:
    steps: List[str]
    executed: int
    timestamp: str


class RunnerUtils:
    @staticmethod
    def run(steps: List[str], payload: Dict[str, Any]) -> RunnerReport:
        executed = sum(1 for step in steps if payload.get(step) is not None)
        return RunnerReport(
            steps=list(steps),
            executed=executed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
