#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
time_utils.py — N243 Time Utils

Rôle :
- Fournir des opérations temporelles simples
- now_utc, isoformat, format_hhmmss
- Publier un rapport temporel
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional


@dataclass
class TimeReport:
    operation: str
    result: str
    timestamp: str


class TimeUtils:
    @staticmethod
    def now_utc() -> datetime:
        return datetime.now(timezone.utc)

    @staticmethod
    def isoformat(value: Optional[datetime] = None) -> str:
        if value is None:
            value = TimeUtils.now_utc()
        return value.isoformat()

    @staticmethod
    def format_hhmmss(value: Optional[datetime] = None) -> str:
        if value is None:
            value = TimeUtils.now_utc()
        return value.strftime("%H:%M:%S")

    @staticmethod
    def report(operation: str, result: str) -> TimeReport:
        return TimeReport(
            operation=operation,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
