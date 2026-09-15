#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
stage_utils.py — N243 Stage Utils

Rôle :
- Fournir un outil d’étape simple
- Publier un rapport d’étape
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class StageReport:
    reached: List[str]
    timestamp: str


class StageUtils:
    @staticmethod
    def advance(stages: List[str], payload: Dict[str, Any]) -> StageReport:
        reached = [stage for stage in stages if payload.get(stage) is True]
        return StageReport(
            reached=reached,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
