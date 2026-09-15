#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_utils.py — N243 Audit Utils

Rôle :
- Fournir un outil d’audit simple
- Publier un rapport d’audit
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class AuditReport:
    audited: List[str]
    timestamp: str


class AuditUtils:
    @staticmethod
    def review(items: List[str], payload: Dict[str, Any]) -> AuditReport:
        audited = [item for item in items if payload.get(item) is not None]
        return AuditReport(
            audited=audited,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
