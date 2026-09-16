#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
channel_utils.py — N243 Channel Utils

Rôle :
- Fournir un outil de canal simple
- Publier un rapport de canal
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ChannelReport:
    routed: List[str]
    timestamp: str


class ChannelUtils:
    @staticmethod
    def inspect(channels: List[str], payload: Dict[str, Any]) -> ChannelReport:
        routed = [channel for channel in channels if payload.get(channel) is True]
        return ChannelReport(
            routed=routed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
