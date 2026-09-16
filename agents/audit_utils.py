#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_utils.py — N24 N243 Audit Utils

Rôle :
- Fournir un outil simple d'audit
- Publier un rapport d'audits effectués
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class AuditReport:
    audits: List[str]
    timestamp: str


class AuditUtils:
    @staticmethod
    def inspect(audits: List[str]) -> AuditReport:
        return AuditReport(
            audits=list(audits),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
