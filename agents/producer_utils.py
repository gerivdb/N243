#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
producer_utils.py — N24 N243 Producer Utils

Rôle :
- Fournir un outil de producteur simple
- Publier un rapport de production
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ProducerReport:
    produced: List[str]
    timestamp: str


class ProducerUtils:
    @staticmethod
    def inspect(targets: List[str], payload: Dict[str, Any]) -> ProducerReport:
        produced = [target for target in targets if payload.get(target) is True]
        return ProducerReport(
            produced=produced,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
