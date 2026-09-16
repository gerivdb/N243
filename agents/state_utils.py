#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
state_utils.py — N24 N243 State Utils

Rôle :
- Fournir un outil simple de gestion d'états
- Publier un rapport d'états observés
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class StateReport:
    states: List[str]
    timestamp: str


class StateUtils:
    @staticmethod
    def inspect(states: List[str]) -> StateReport:
        return StateReport(
            states=list(states),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
