#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
heartbeat_utils.py — N243 Heartbeat Utils

Rôle :
- Fournir un outil de battement simple
- Publier un rapport de battement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class HeartbeatReport:
    alive: bool
    timestamp: str


class HeartbeatUtils:
    @staticmethod
    def check(payload: Dict[str, Any]) -> HeartbeatReport:
        return HeartbeatReport(
            alive=payload.get("alive", False),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
