#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chunk_utils.py — N24 N243 Chunk Utils

Rôle :
- Fournir un outil simple de gestion de chunks
- Publier un rapport de chunks traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ChunkReport:
    chunks: List[str]
    timestamp: str


class ChunkUtils:
    @staticmethod
    def inspect(chunks: List[str]) -> ChunkReport:
        return ChunkReport(
            chunks=list(chunks),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
