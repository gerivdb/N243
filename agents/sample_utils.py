#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sample_utils.py — N243 Sample Utils

Rôle :
- Fournir un outil de sampling simple
- Publier un rapport de sampling
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class SampleReport:
    sampled: List[str]
    timestamp: str


class SampleUtils:
    @staticmethod
    def pick(items: List[str], payload: Dict[str, Any]) -> SampleReport:
        sampled = [item for item in items if payload.get(item) is True]
        return SampleReport(
            sampled=sampled,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
