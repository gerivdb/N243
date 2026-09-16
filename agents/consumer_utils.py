#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
consumer_utils.py — N243 Consumer Utils

Rôle :
- Fournir un outil de consommation simple
- Publier un rapport de consommation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ConsumerReport:
    consumed: List[str]
    timestamp: str


class ConsumerUtils:
    @staticmethod
    def inspect(targets: List[str], payload: Dict[str, Any]) -> ConsumerReport:
        consumed = [target for target in targets if payload.get(target) is True]
        return ConsumerReport(
            consumed=consumed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
