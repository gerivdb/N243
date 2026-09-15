#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resume_utils.py — N243 Resume Utils

Rôle :
- Fournir un outil de reprise simple
- Publier un rapport de reprise
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ResumeReport:
    resumed: List[Any]
    timestamp: str


class ResumeUtils:
    @staticmethod
    def filter(payloads: List[Dict[str, Any]]) -> ResumeReport:
        resumed = [payload.get("value") for payload in payloads if payload.get("resume", False)]
        return ResumeReport(
            resumed=resumed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
