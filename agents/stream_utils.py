#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
stream_utils.py — N243 Stream Utils

Rôle :
- Fournir des utilitaires pour le streaming/accumulation
- Découper un flux en paquets
- Publier un rapport par paquet
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Iterable, List


@dataclass
class StreamResult:
    operation: str
    chunk_index: int
    chunk_size: int
    timestamp: str


class StreamUtils:
    @staticmethod
    def chunk_items(items: List[Any], size: int) -> List[List[Any]]:
        if size <= 0:
            raise ValueError("size must be > 0")
        return [items[i:i + size] for i in range(0, len(items), size)]

    @staticmethod
    def consume(items: Iterable[Any], consumer: Callable[[Any], None]) -> None:
        for item in items:
            consumer(item)

    def report(self, operation: str, chunk_index: int, chunk_size: int) -> StreamResult:
        return StreamResult(
            operation=operation,
            chunk_index=chunk_index,
            chunk_size=chunk_size,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
