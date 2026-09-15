#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
session_utils.py — N243 Session Utils

Rôle :
- Fournir un outil de session simple
- Publier un rapport de session
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class SessionReport:
    started: List[str]
    timestamp: str


class SessionUtils:
    @staticmethod
    def manage(sessions: List[str], payload: Dict[str, Any]) -> SessionReport:
        started = [session for session in sessions if payload.get(session) is True]
        return SessionReport(
            started=started,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
