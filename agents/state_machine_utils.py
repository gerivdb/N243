#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
state_machine_utils.py — N243 State Machine Utils

Rôle :
- Fournir une machine à états simple
- Gérer des transitions d'état autorisées
- Publier un rapport d'état
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class StateReport:
    current: str
    previous: Optional[str]
    allowed: List[str]
    timestamp: str


class StateMachineUtils:
    def __init__(self, initial: str, allowed: Optional[List[str]] = None) -> None:
        self._current = initial
        self._allowed = set(allowed or [initial])
        self._previous: Optional[str] = None

    def can_transit(self, target: str) -> bool:
        return target in self._allowed

    def transit(self, target: str) -> bool:
        if not self.can_transit(target):
            return False
        self._previous = self._current
        self._current = target
        return True

    def state(self) -> str:
        return self._current

    def report(self) -> StateReport:
        return StateReport(
            current=self._current,
            previous=self._previous,
            allowed=sorted(self._allowed),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
