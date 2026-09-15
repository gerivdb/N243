#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
profile_utils.py — N243 Profile Utils

Rôle :
- Fournir un outil de profiling simple
- Publier un rapport de profiling
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ProfileReport:
    profiled: List[str]
    timestamp: str


class ProfileUtils:
    @staticmethod
    def measure(targets: List[str], payload: Dict[str, Any]) -> ProfileReport:
        profiled = [target for target in targets if payload.get(target) is not None]
        return ProfileReport(
            profiled=profiled,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
