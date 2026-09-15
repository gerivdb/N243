#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tracer_utils.py — N243 Tracer Utils

Rôle :
- Fournir un outil de traçage simple
- Publier un rapport de traçage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class TracerReport:
    traced: List[str]
    timestamp: str


class TracerUtils:
    @staticmethod
    def follow(items: List[str], payload: Dict[str, Any]) -> TracerReport:
        traced = [item for item in items if payload.get(item) is not None]
        return TracerReport(
            traced=traced,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
