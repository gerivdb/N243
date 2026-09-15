#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chunk_utils.py — N243 Chunk Utils

Rôle :
- Fournir un outil de découpage simple
- Publier un rapport de découpage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ChunkReport:
    chunks: List[List[Any]]
    timestamp: str


class ChunkUtils:
    @staticmethod
    def apply(values: List[Any], size: int) -> ChunkReport:
        chunks = [values[index:index + size] for index in range(0, len(values), size)]
        return ChunkReport(
            chunks=chunks,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
