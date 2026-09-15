#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
process_utils.py — N243 Process Utils

Rôle :
- Fournir un moteur de traitement simple
- Publier un rapport de traitement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ProcessReport:
    processed: List[str]
    failed: List[str]
    timestamp: str


class ProcessUtils:
    @staticmethod
    def run(steps: List[str], payload: Dict[str, Any]) -> ProcessReport:
        processed = [step for step in steps if payload.get(step) is True]
        failed = [step for step in steps if payload.get(step) is False]
        return ProcessReport(
            processed=processed,
            failed=failed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
