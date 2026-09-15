#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
buffer_utils.py — N243 Buffer Utils

Rôle :
- Fournir un buffer simple de type FIFO
- Ajouter des éléments, vider le buffer
- Publier un rapport de buffer
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class BufferReport:
    size: int
    items: List[Any]
    timestamp: str


class BufferUtils:
    def __init__(self, maxlen: int = 10) -> None:
        self._buffer: deque = deque(maxlen=maxlen)

    def add(self, item: Any) -> None:
        self._buffer.append(item)

    def drain(self) -> List[Any]:
        return list(self._buffer)

    def report(self) -> BufferReport:
        return BufferReport(
            size=len(self._buffer),
            items=list(self._buffer),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
