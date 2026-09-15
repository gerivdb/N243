#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
recovery_utils.py — N243 Recovery Utils

Rôle :
- Fournir un outil de rétablissement simple
- Publier un rapport de rétablissement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class RecoveryReport:
    recovered: List[Any]
    timestamp: str


class RecoveryUtils:
    @staticmethod
    def filter(payloads: List[Dict[str, Any]]) -> RecoveryReport:
        recovered = [payload.get("value") for payload in payloads if payload.get("recovery", False)]
        return RecoveryReport(
            recovered=recovered,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
