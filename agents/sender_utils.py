#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sender_utils.py — N243 Sender Utils

Rôle :
- Fournir un outil d’envoi simple
- Publier un rapport d’envoi
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class SenderReport:
    sent: List[str]
    timestamp: str


class SenderUtils:
    @staticmethod
    def inspect(targets: List[str], payload: Dict[str, Any]) -> SenderReport:
        sent = [target for target in targets if payload.get(target) is True]
        return SenderReport(
            sent=sent,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
