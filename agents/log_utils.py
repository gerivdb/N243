#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
log_utils.py — N24 N243 Log Utils

Rôle :
- Fournir un outil simple de gestion de logs
- Publier un rapport de logs traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class LogReport:
    logs: List[str]
    timestamp: str


class LogUtils:
    @staticmethod
    def inspect(logs: List[str]) -> LogReport:
        return LogReport(
            logs=list(logs),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
