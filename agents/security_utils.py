#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
security_utils.py — N24 N243 Security Utils

Rôle :
- Fournir un outil simple de gestion de sécurité
- Publier un rapport de checks sécurité
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class SecurityReport:
    checks: List[str]
    timestamp: str


class SecurityUtils:
    @staticmethod
    def inspect(checks: List[str]) -> SecurityReport:
        return SecurityReport(
            checks=list(checks),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
