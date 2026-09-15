#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
frame_utils.py — N243 Frame Utils

Rôle :
- Fournir un outil de trame simple
- Découper une série en blocs
- Publier un rapport de trame
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class FrameReport:
    frames: int
    timestamp: str


class FrameUtils:
    @staticmethod
    def chunk(values: List[Any], size: int) -> Dict[int, List[Any]]:
        frames: Dict[int, List[Any]] = {}
        for i in range(0, len(values), size):
            frames[len(frames)] = values[i : i + size]
        return frames

    def report(self, values: List[Any], size: int) -> FrameReport:
        frames = self.chunk(values, size)
        return FrameReport(
            frames=len(frames),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
