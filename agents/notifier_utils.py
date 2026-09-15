#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
notifier_utils.py — N243 Notifier Utils

Rôle :
- Fournir un système de notification simple
- Envoyer des messages à des abonnés
- Publier un rapport de notification
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass
class NotifyResult:
    message: str
    subscribers: int
    timestamp: str


class NotifierUtils:
    def __init__(self) -> None:
        self._subscribers: Dict[str, List[Callable[[str], None]]] = {}

    def subscribe(self, topic: str, handler: Callable[[str], None]) -> None:
        self._subscribers.setdefault(topic, []).append(handler)

    def notify(self, topic: str, message: str) -> None:
        for handler in self._subscribers.get(topic, []):
            handler(message)

    def subscriber_count(self, topic: str) -> int:
        return len(self._subscribers.get(topic, []))

    def report(self, topic: str, message: str) -> NotifyResult:
        return NotifyResult(
            message=message,
            subscribers=self.subscriber_count(topic),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
