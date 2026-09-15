#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
notifier_utils.py — N243 Notifier Utils

Rôle :
- Fournir un outil de notification simple
- Publier un rapport de notification
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class NotifierReport:
    notified: List[str]
    timestamp: str


class NotifierUtils:
    @staticmethod
    def send(targets: List[str], payload: Dict[str, Any]) -> NotifierReport:
        notified = [target for target in targets if payload.get(target) is True]
        return NotifierReport(
            notified=notified,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
