#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
exception_utils.py — N243 Exception Utils

Rôle :
- Fournir un outil d’exception simple
- Publier un rapport d’exception
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ExceptionReport:
    caught: List[str]
    timestamp: str


class ExceptionUtils:
    @staticmethod
    def track(names: List[str], payload: Dict[str, Any]) -> ExceptionReport:
        caught = [name for name in names if payload.get(name) is True]
        return ExceptionReport(
            caught=caught,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
