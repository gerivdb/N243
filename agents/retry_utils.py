#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
retry_utils.py — N24 N243 Retry Utils

Rôle :
- Fournir un outil simple de gestion de retries
- Publier un rapport d'opérations retryées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class RetryReport:
    retried: List[str]
    timestamp: str


class RetryUtils:
    @staticmethod
    def inspect(retried: List[str]) -> RetryReport:
        return RetryReport(
            retried=list(retried),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
