#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
migration_utils.py — N243 Migration Utils

Rôle :
- Fournir un outil de migration simple
- Publier un rapport de migration
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class MigrationReport:
    migrated: List[Any]
    timestamp: str


class MigrationUtils:
    @staticmethod
    def filter(payloads: List[Dict[str, Any]]) -> MigrationReport:
        migrated = [payload.get("value") for payload in payloads if payload.get("migration", False)]
        return MigrationReport(
            migrated=migrated,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
