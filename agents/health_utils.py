#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
health_utils.py — N24 N243 Health Utils

Rôle :
- Fournir un outil simple de gestion de santé système
- Publier un rapport de checks santé
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class HealthReport:
    checks: List[str]
    timestamp: str


class HealthUtils:
    @staticmethod
    def inspect(checks: List[str]) -> HealthReport:
        return HealthReport(
            checks=list(checks),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
