#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redundancy_utils.py — N243 Redundancy Utils

Rôle :
- Fournir un outil de redondance simple
- Publier un rapport de redondance
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class RedundancyReport:
    redundant: List[Any]
    timestamp: str


class RedundancyUtils:
    @staticmethod
    def filter(payloads: List[Dict[str, Any]]) -> RedundancyReport:
        redundant = [payload.get("value") for payload in payloads if payload.get("redundant", False)]
        return RedundancyReport(
            redundant=redundant,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
