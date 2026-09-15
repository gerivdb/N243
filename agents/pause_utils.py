#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pause_utils.py — N243 Pause Utils

Rôle :
- Fournir un outil de pause simple
- Publier un rapport de pause
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class PauseReport:
    paused: List[Any]
    timestamp: str


class PauseUtils:
    @staticmethod
    def filter(payloads: List[Dict[str, Any]]) -> PauseReport:
        paused = [payload.get("value") for payload in payloads if payload.get("paused", False)]
        return PauseReport(
            paused=paused,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
