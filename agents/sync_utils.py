#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_utils.py — N24 N243 Sync Utils

Rôle :
- Fournir un outil simple de synchronisation
- Publier un rapport de synchronisations effectuées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class SyncReport:
    syncs: List[str]
    timestamp: str


class SyncUtils:
    @staticmethod
    def inspect(syncs: List[str]) -> SyncReport:
        return SyncReport(
            syncs=list(syncs),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
