#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
snapshot_utils.py — N243 Snapshot Utils

Rôle :
- Fournir un outil de snapshot simple
- Publier un rapport de snapshot
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class SnapshotReport:
    captured: List[str]
    timestamp: str


class SnapshotUtils:
    @staticmethod
    def capture(items: List[str], payload: Dict[str, Any]) -> SnapshotReport:
        captured = [item for item in items if payload.get(item) is not None]
        return SnapshotReport(
            captured=captured,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
