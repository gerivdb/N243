#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
step_utils.py — N243 Step Utils

Rôle :
- Fournir un outil d’étape atomique simple
- Publier un rapport d’étape
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class StepReport:
    advanced: List[str]
    timestamp: str


class StepUtils:
    @staticmethod
    def advance(steps: List[str], payload: Dict[str, Any]) -> StepReport:
        advanced = [step for step in steps if payload.get(step) is True]
        return StepReport(
            advanced=advanced,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
