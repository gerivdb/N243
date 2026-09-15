#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
router_utils.py — N243 Router Utils

Rôle :
- Fournir un routeur simple par clé
- Diriger des entrées vers des handlers
- Publier un rapport de routage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, Optional


@dataclass
class RouteResult:
    key: str
    handled: bool
    result: Any
    error: Optional[str]
    timestamp: str


class RouterUtils:
    def __init__(self, routes: Dict[str, Callable[[Any], Any]]) -> None:
        self._routes = routes

    def route(self, key: str, payload: Any) -> RouteResult:
        handler = self._routes.get(key)
        if handler is None:
            return RouteResult(
                key=key,
                handled=False,
                result=None,
                error="no route",
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
        try:
            result = handler(payload)
            return RouteResult(
                key=key,
                handled=True,
                result=result,
                error=None,
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
        except Exception as exc:  # noqa: BLE001
            return RouteResult(
                key=key,
                handled=True,
                result=None,
                error=str(exc),
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
