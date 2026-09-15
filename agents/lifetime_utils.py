#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lifetime_utils.py — N243 Lifetime Utils

Rôle :
- Fournir un gestionnaire de cycle de vie simple
- Suivre les états : created, active, paused, completed
- Publier un rapport de cycle de vie
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class LifecycleReport:
    state: str
    history: List[str]
    timestamp: str


class LifetimeUtils:
    CREATED = "created"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"

    def __init__(self) -> None:
        self._state: str = self.CREATED
        self._history: List[str] = [self.CREATED]

    def set_state(self, state: str) -> None:
        self._state = state
        self._history.append(state)

    def state(self) -> str:
        return self._state

    def history(self) -> List[str]:
        return list(self._history)

    def report(self) -> LifecycleReport:
        return LifecycleReport(
            state=self._state,
            history=list(self._history),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
