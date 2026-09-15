#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
release_utils.py — N243 Release Utils

Rôle :
- Fournir un outil de libération simple
- Publier un rapport de libération
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ReleaseReport:
    released: List[float]
    timestamp: str


class ReleaseUtils:
    @staticmethod
    def below(values: List[float], threshold: float) -> ReleaseReport:
        released = [value for value in values if value < threshold]
        return ReleaseReport(
            released=released,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
