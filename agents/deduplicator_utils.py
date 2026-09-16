#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deduplicator_utils.py — N24 N243 Deduplicator Utils

Rôle :
- Fournir un outil simple de déduplication
- Publier un rapport de doublons détectés
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class DedupReport:
    duplicates: List[str]
    timestamp: str


class DeduplicatorUtils:
    @staticmethod
    def inspect(duplicates: List[str]) -> DedupReport:
        return DedupReport(
            duplicates=list(duplicates),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
