#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
interrupt_utils.py — N243 Interrupt Utils

Rôle :
- Fournir un outil d'interruption simple
- Publier un rapport d'interruption
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class InterruptReport:
    interrupted: int
    timestamp: str


class InterruptUtils:
    @staticmethod
    def check(payloads: List[Dict[str, Any]], threshold: float) -> InterruptReport:
        interrupted = sum(1 for payload in payloads if payload.get("value", 0) >= threshold)
        return InterruptReport(
            interrupted=interrupted,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
