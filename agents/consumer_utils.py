#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
consumer_utils.py — N243 Consumer Utils

Rôle :
- Fournir un consommateur simple de valeurs
- Enregistrer des consommateurs, déclencher des callbacks
- Publier un rapport de consommation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass
class ConsumerResult:
    topic: str
    consumed: bool
    payload: Any
    timestamp: str


class ConsumerUtils:
    def __init__(self) -> None:
        self._consumers: Dict[str, List[Callable[[Any], None]]] = {}

    def subscribe(self, topic: str, handler: Callable[[Any], None]) -> None:
        self._consumers.setdefault(topic, []).append(handler)

    def consume(self, topic: str, payload: Any) -> None:
        for handler in self._consumers.get(topic, []):
            handler(payload)

    def report(self, topic: str, consumed: bool, payload: Any) -> ConsumerResult:
        return ConsumerResult(
            topic=topic,
            consumed=consumed,
            payload=payload,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
