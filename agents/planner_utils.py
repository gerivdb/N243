#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
planner_utils.py — N243 Planner Utils

Rôle :
- Fournir un planificateur simple pour des tâches
- Planifier des étapes avec dépendances
- Publier un rapport de planification
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class PlanResult:
    steps: int
    plan: List[str]
    timestamp: str


class PlannerUtils:
    def __init__(self) -> None:
        self._steps: List[str] = []

    def add_step(self, step: str) -> None:
        self._steps.append(step)

    def plan(self) -> List[str]:
        return list(self._steps)

    def report(self) -> PlanResult:
        return PlanResult(
            steps=len(self._steps),
            plan=list(self._steps),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
