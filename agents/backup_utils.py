#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
backup_utils.py — N243 Backup Utils

Rôle :
- Fournir un outil de sauvegarde simple
- Publier un rapport de sauvegarde
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class BackupReport:
    backup: List[Any]
    timestamp: str


class BackupUtils:
    @staticmethod
    def filter(payloads: List[Dict[str, Any]]) -> BackupReport:
        backup = [payload.get("value") for payload in payloads if payload.get("backup", False)]
        return BackupReport(
            backup=backup,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
