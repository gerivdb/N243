#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
shutdown_utils.py — N243 Shutdown Utils

Rôle :
- Fournir un outil d'arrêt simple
- Publier un rapport d'arrêt
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ShutdownReport:
    shutdown: List[Any]
    timestamp: str


class ShutdownUtils:
    @staticmethod
    def filter(payloads: List[Dict[str, Any]]) -> ShutdownReport:
        shutdown = [payload.get("value") for payload in payloads if payload.get("shutdown", False)]
        return ShutdownReport(
            shutdown=shutdown,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
