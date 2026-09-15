#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pipeline_utils.py — N243 Pipeline Utils

Rôle :
- Fournir un pipeline simple
- Publier un rapport de pipeline
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class PipelineReport:
    stages: List[str]
    completed: int
    timestamp: str


class PipelineUtils:
    @staticmethod
    def run(stages: List[str], payload: Dict[str, Any]) -> PipelineReport:
        completed = sum(1 for stage in stages if payload.get(stage) is True)
        return PipelineReport(
            stages=list(stages),
            completed=completed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
