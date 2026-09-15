#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
memory_utils.py — N243 Memory Utils

Rôle :
- Fournir un outil de mémoire simple
- Publier un rapport de mémoire
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class MemoryReport:
    stored: List[str]
    timestamp: str


class MemoryUtils:
    @staticmethod
    def store(keys: List[str], payload: Dict[str, Any]) -> MemoryReport:
        stored = [key for key in keys if payload.get(key) is not None]
        return MemoryReport(
            stored=stored,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
