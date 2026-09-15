#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
downgrade_utils.py — N243 Downgrade Utils

Rôle :
- Fournir un outil de descente simple
- Publier un rapport de descente
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class DowngradeReport:
    downgraded: List[Any]
    timestamp: str


class DowngradeUtils:
    @staticmethod
    def filter(payloads: List[Dict[str, Any]]) -> DowngradeReport:
        downgraded = [payload.get("value") for payload in payloads if payload.get("downgrade", False)]
        return DowngradeReport(
            downgraded=downgraded,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
