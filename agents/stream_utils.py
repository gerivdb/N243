#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
stream_utils.py — N243 Stream Utils

Rôle :
- Fournir un outil de flux simple
- Publier un rapport de flux
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class StreamReport:
    streamed: List[str]
    timestamp: str


class StreamUtils:
    @staticmethod
    def inspect(targets: List[str], payload: Dict[str, Any]) -> StreamReport:
        streamed = [target for target in targets if payload.get(target) is True]
        return StreamReport(
            streamed=streamed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
