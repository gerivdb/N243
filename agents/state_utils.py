#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
state_utils.py — N243 State Utils

Rôle :
- Fournir un outil d'état simple
- Mémoriser un état booléen
- Publier un rapport d'état
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class StateReport:
    state: Dict[str, Any]
    timestamp: str


class StateUtils:
    @staticmethod
    def update(state: Dict[str, Any], key: str, value: Any) -> StateReport:
        state[key] = value
        return StateReport(
            state=dict(state),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
