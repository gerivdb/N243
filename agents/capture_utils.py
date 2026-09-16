#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
capture_utils.py — N24 N243 Capture Utils

Rôle :
- Fournir un outil simple de capture
- Publier un rapport de captures effectuées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class CaptureReport:
    captures: List[str]
    timestamp: str


class CaptureUtils:
    @staticmethod
    def inspect(captures: List[str]) -> CaptureReport:
        return CaptureReport(
            captures=list(captures),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
