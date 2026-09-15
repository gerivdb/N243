#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
refresher_utils.py — N243 Refresher Utils

Rôle :
- Fournir un rafraîchisseur simple pour des états
- Réinitialiser des compteurs, vider des caches
- Publier un rapport de rafraîchissement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class RefreshResult:
    target: str
    previous: Any
    current: Any
    timestamp: str


class RefresherUtils:
    def __init__(self) -> None:
        self._store: Dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        self._store[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._store.get(key, default)

    def refresh(self, key: str, factory) -> Any:
        previous = self._store.get(key)
        current = factory()
        self._store[key] = current
        return current

    def report(self, key: str, previous: Any, current: Any) -> RefreshResult:
        return RefreshResult(
            target=key,
            previous=previous,
            current=current,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
