#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
event_utils.py — N243 Event Utils

Rôle :
- Fournir un système d'événements simple
- S'abonner, publier, se désabonner
- Publier un rapport d'état
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass
class EventReport:
    event: str
    listeners: int
    last_payload: Any
    timestamp: str


class EventUtils:
    def __init__(self) -> None:
        self._listeners: Dict[str, List[Callable[[Any], None]]] = {}

    def subscribe(self, event: str, handler: Callable[[Any], None]) -> None:
        self._listeners.setdefault(event, []).append(handler)

    def publish(self, event: str, payload: Any) -> None:
        for handler in self._listeners.get(event, []):
            handler(payload)

    def unsubscribe(self, event: str, handler: Callable[[Any], None]) -> None:
        handlers = self._listeners.get(event, [])
        self._listeners[event] = [h for h in handlers if h is not handler]

    def listener_count(self, event: str) -> int:
        return len(self._listeners.get(event, []))

    def report(self, event: str, payload: Any) -> EventReport:
        return EventReport(
            event=event,
            listeners=self.listener_count(event),
            last_payload=payload,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
