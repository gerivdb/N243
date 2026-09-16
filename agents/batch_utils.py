#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
batch_utils.py — N24 N243 Batch Utils

Rôle :
- Fournir un outil simple de gestion de lot
- Publier un rapport de lots traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class BatchReport:
    batches: List[str]
    timestamp: str


class BatchUtils:
    @staticmethod
    def inspect(batches: List[str]) -> BatchReport:
        return BatchReport(
            batches=list(batches),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
