#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
workflow_utils.py — N243 Workflow Utils

Rôle :
- Fournir un outil de workflow simple
- Publier un rapport de workflow
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class WorkflowReport:
    executed: List[str]
    timestamp: str


class WorkflowUtils:
    @staticmethod
    def run(steps: List[str], payload: Dict[str, Any]) -> WorkflowReport:
        executed = [step for step in steps if payload.get(step) is True]
        return WorkflowReport(
            executed=executed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
