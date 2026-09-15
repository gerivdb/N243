#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
receiver_utils.py — N243 Receiver Utils

Rôle :
- Fournir un outil de réception simple
- Publier un rapport de réception
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ReceiverReport:
    received: List[str]
    timestamp: str


class ReceiverUtils:
    @staticmethod
    def inspect(targets: List[str], payload: Dict[str, Any]) -> ReceiverReport:
        received = [target for target in targets if payload.get(target) is True]
        return ReceiverReport(
            received=received,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
