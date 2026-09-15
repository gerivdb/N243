#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
retry_utils.py — N243 Retry Utils

Rôle :
- Fournir un moteur de réessai simple et borné
- Appliquer un délai fixe entre les tentatives
- Publier un rapport par tentative
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, List, Optional


@dataclass
class RetryReport:
    attempt: int
    success: bool
    value: Any
    error: Optional[str]
    timestamp: str


class RetryUtils:
    def run(self, func: Callable[[], Any], attempts: int, delay: float = 0.0) -> RetryReport:
        last_error: Optional[str] = None
        for attempt in range(1, attempts + 1):
            try:
                value = func()
                return RetryReport(
                    attempt=attempt,
                    success=True,
                    value=value,
                    error=None,
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
            except Exception as exc:  # noqa: BLE001
                last_error = str(exc)
                if attempt < attempts and delay > 0:
                    time.sleep(delay)
        return RetryReport(
            attempt=attempts,
            success=False,
            value=None,
            error=last_error,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
