#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
channel_utils.py — N24 N243 Channel Utils

Rôle :
- Fournir un outil simple de gestion de canaux
- Publier un rapport de canaux traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ChannelReport:
    channels: List[str]
    timestamp: str


class ChannelUtils:
    @staticmethod
    def inspect(channels: List[str]) -> ChannelReport:
        return ChannelReport(
            channels=list(channels),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
