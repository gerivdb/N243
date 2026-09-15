#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
work_utils.py — N243 Work Utils

Rôle :
- Fournir un outil de travail simple
- Publier un rapport de travail
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class WorkReport:
    items: List[str]
    processed: int
    timestamp: str


class WorkUtils:
    @staticmethod
    def process(items: List[str], payload: Dict[str, Any]) -> WorkReport:
        processed = sum(1 for item in items if payload.get(item) is not None)
        return WorkReport(
            items=list(items),
            processed=processed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
