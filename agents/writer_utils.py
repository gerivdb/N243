#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
writer_utils.py — N243 Writer Utils

Rôle :
- Fournir un outil d’écriture simple
- Publier un rapport d’écriture
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class WriterReport:
    written: List[str]
    timestamp: str


class WriterUtils:
    @staticmethod
    def inspect(targets: List[str], payload: Dict[str, Any]) -> WriterReport:
        written = [target for target in targets if payload.get(target) is True]
        return WriterReport(
            written=written,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
