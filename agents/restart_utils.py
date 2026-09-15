#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
restart_utils.py — N243 Restart Utils

Rôle :
- Fournir un outil de redémarrage simple
- Publier un rapport de redémarrage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class RestartReport:
    restarted: List[Any]
    timestamp: str


class RestartUtils:
    @staticmethod
    def filter(payloads: List[Dict[str, Any]]) -> RestartReport:
        restarted = [payload.get("value") for payload in payloads if payload.get("restart", False)]
        return RestartReport(
            restarted=restarted,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
