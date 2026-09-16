#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
router_utils.py — N243 Router Utils

Rôle :
- Fournir un outil de routage simple
- Publier un rapport de routage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class RouterReport:
    routed: List[str]
    timestamp: str


class RouterUtils:
    @staticmethod
    def inspect(routes: List[str], payload: Dict[str, Any]) -> RouterReport:
        routed = [route for route in routes if payload.get(route) is True]
        return RouterReport(
            routed=routed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
