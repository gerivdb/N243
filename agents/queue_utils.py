#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
queue_utils.py — N243 Queue Utils

Rôle :
- Fournir un outil de file simple
- Publier un rapport de file
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class QueueReport:
    queued: List[str]
    timestamp: str


class QueueUtils:
    @staticmethod
    def inspect(queues: List[str], payload: Dict[str, Any]) -> QueueReport:
        queued = [queue for queue in queues if payload.get(queue) is True]
        return QueueReport(
            queued=queued,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
