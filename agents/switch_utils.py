#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
switch_utils.py — N243 Switch Utils

Rôle :
- Fournir un outil de commutation simple
- Sélectionner une valeur par condition
- Publier un rapport de commutation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class SwitchReport:
    selected: Any
    condition: str
    timestamp: str


class SwitchUtils:
    @staticmethod
    def select(conditions: Dict[str, Any], default: Any = None) -> SwitchReport:
        for condition, value in conditions.items():
            if value:
                return SwitchReport(
                    selected=value,
                    condition=condition,
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
        return SwitchReport(
            selected=default,
            condition="default",
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
