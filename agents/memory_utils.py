#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
memory_utils.py — N24 N243 Memory Utils

Rôle :
- Fournir un outil simple de gestion de mémoire
- Publier un rapport de blocs mémoire traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class MemoryReport:
    blocks: List[str]
    timestamp: str


class MemoryUtils:
    @staticmethod
    def inspect(blocks: List[str]) -> MemoryReport:
        return MemoryReport(
            blocks=list(blocks),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
