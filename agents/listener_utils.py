#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
listener_utils.py — N243 Listener Utils

Rôle :
- Fournir un écouteur simple pour des événements
- Enregistrer des callbacks, déclencher des écouteurs
- Publier un rapport d'écoute
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass
class ListenResult:
    event: str
    listeners_called: int
    timestamp: str


class ListenerUtils:
    def __init__(self) -> None:
        self._listeners: Dict[str, List[Callable[[Any], None]]] = {}

    def on(self, event: str, handler: Callable[[Any], None]) -> None:
        self._listeners.setdefault(event, []).append(handler)

    def emit(self, event: str, payload: Any) -> None:
        for handler in self._listeners.get(event, []):
            handler(payload)

    def listener_count(self, event: str) -> int:
        return len(self._listeners.get(event, []))

    def report(self, event: str, payload: Any) -> ListenResult:
        self.emit(event, payload)
        return ListenResult(
            event=event,
            listeners_called=self.listener_count(event),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
