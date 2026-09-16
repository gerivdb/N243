#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
buffer_utils.py — N243 Buffer Utils

Rôle :
- Fournir un outil de tampon simple
- Publier un rapport de tampon
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class BufferReport:
    buffered: List[str]
    timestamp: str


class BufferUtils:
    @staticmethod
    def inspect(buffers: List[str], payload: Dict[str, Any]) -> BufferReport:
        buffered = [buffer for buffer in buffers if payload.get(buffer) is True]
        return BufferReport(
            buffered=buffered,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
