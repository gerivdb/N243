#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
checker_utils.py — N24 N243 Checker Utils

Rôle :
- Fournir un outil simple de vérification
- Publier un rapport de checks effectués
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class CheckReport:
    checks: List[str]
    timestamp: str


class CheckerUtils:
    @staticmethod
    def inspect(checks: List[str]) -> CheckReport:
        return CheckReport(
            checks=list(checks),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
