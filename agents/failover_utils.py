#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
failover_utils.py — N243 Failover Utils

Rôle :
- Fournir un outil de basculement simple
- Publier un rapport de basculement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class FailoverReport:
    active: str
    timestamp: str


class FailoverUtils:
    @staticmethod
    def select(payloads: List[Dict[str, Any]], primary: str) -> FailoverReport:
        for payload in payloads:
            if payload.get("name") == primary and payload.get("alive", False):
                return FailoverReport(
                    active=primary,
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
        fallback = next((payload.get("name") for payload in payloads if payload.get("alive", False)), primary)
        return FailoverReport(
            active=fallback,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
