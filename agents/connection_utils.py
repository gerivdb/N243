#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
connection_utils.py — N243 Connection Utils

Rôle :
- Fournir un outil de connexion simple
- Publier un rapport de connexion
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ConnectionReport:
    connected: List[str]
    timestamp: str


class ConnectionUtils:
    @staticmethod
    def inspect(endpoints: List[str], payload: Dict[str, Any]) -> ConnectionReport:
        connected = [endpoint for endpoint in endpoints if payload.get(endpoint) is True]
        return ConnectionReport(
            connected=connected,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
