#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
backup_utils.py — N24 N243 Backup Utils

Rôle :
- Fournir un outil simple de gestion de sauvegarde
- Publier un rapport de sauvegardes effectuées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class BackupReport:
    backups: List[str]
    timestamp: str


class BackupUtils:
    @staticmethod
    def inspect(backups: List[str]) -> BackupReport:
        return BackupReport(
            backups=list(backups),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
