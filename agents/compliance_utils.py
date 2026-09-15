#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compliance_utils.py — N243 Compliance Utils

Rôle :
- Fournir un outil de conformité simple
- Publier un rapport de conformité
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ComplianceReport:
    compliant: List[str]
    timestamp: str


class ComplianceUtils:
    @staticmethod
    def check(items: List[str], payload: Dict[str, Any]) -> ComplianceReport:
        compliant = [item for item in items if payload.get(item) is True]
        return ComplianceReport(
            compliant=compliant,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
