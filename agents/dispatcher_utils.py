#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dispatcher_utils.py — N243 Dispatcher Utils

Rôle :
- Fournir un outil de dispatch simple
- Publier un rapport de dispatch
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class DispatcherReport:
    dispatched: List[str]
    timestamp: str


class DispatcherUtils:
    @staticmethod
    def inspect(targets: List[str], payload: Dict[str, Any]) -> DispatcherReport:
        dispatched = [target for target in targets if payload.get(target) is True]
        return DispatcherReport(
            dispatched=dispatched,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
