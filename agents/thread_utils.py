#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
thread_utils.py — N243 Thread Utils

Rôle :
- Fournir un outil de thread simple
- Publier un rapport de thread
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ThreadReport:
    active: List[str]
    timestamp: str


class ThreadUtils:
    @staticmethod
    def inspect(threads: List[str], payload: Dict[str, Any]) -> ThreadReport:
        active = [thread for thread in threads if payload.get(thread) is True]
        return ThreadReport(
            active=active,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
