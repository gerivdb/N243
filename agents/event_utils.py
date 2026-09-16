#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
event_utils.py — N24 N243 Event Utils

Rôle :
- Fournir un outil simple de gestion d'événements
- Publier un rapport d'événements traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class EventReport:
    events: List[str]
    timestamp: str


class EventUtils:
    @staticmethod
    def inspect(events: List[str]) -> EventReport:
        return EventReport(
            events=list(events),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
