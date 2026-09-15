#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
listener_utils.py — N243 Listener Utils

Rôle :
- Fournir un outil d’écoute simple
- Publier un rapport d’écoute
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ListenerReport:
    listening: List[str]
    timestamp: str


class ListenerUtils:
    @staticmethod
    def inspect(listeners: List[str], payload: Dict[str, Any]) -> ListenerReport:
        listening = [listener for listener in listeners if payload.get(listener) is True]
        return ListenerReport(
            listening=listening,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
