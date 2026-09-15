#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
upgrade_utils.py — N243 Upgrade Utils

Rôle :
- Fournir un outil de montée simple
- Publier un rapport de montée
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class UpgradeReport:
    upgraded: List[Any]
    timestamp: str


class UpgradeUtils:
    @staticmethod
    def filter(payloads: List[Dict[str, Any]]) -> UpgradeReport:
        upgraded = [payload.get("value") for payload in payloads if payload.get("upgrade", False)]
        return UpgradeReport(
            upgraded=upgraded,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
