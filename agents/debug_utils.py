#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
debug_utils.py — N243 Debug Utils

Rôle :
- Fournir un outil de débogage simple
- Publier un rapport de débogage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class DebugReport:
    issues: List[str]
    timestamp: str


class DebugUtils:
    @staticmethod
    def inspect(checks: List[str], payload: Dict[str, Any]) -> DebugReport:
        issues = [check for check in checks if payload.get(check) is False]
        return DebugReport(
            issues=issues,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
