#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
handler_utils.py — N243 Handler Utils

Rôle :
- Fournir un gestionnaire d’action simple
- Publier un rapport de traitement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class HandlerReport:
    handled: List[str]
    skipped: List[str]
    timestamp: str


class HandlerUtils:
    @staticmethod
    def dispatch(actions: List[str], payload: Dict[str, Any]) -> HandlerReport:
        handled = [action for action in actions if payload.get(action) is not None]
        skipped = [action for action in actions if payload.get(action) is None]
        return HandlerReport(
            handled=handled,
            skipped=skipped,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
