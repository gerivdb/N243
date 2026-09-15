#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
join_utils.py — N243 Join Utils

Rôle :
- Fournir un outil de jointure simple
- Publier un rapport de jointure
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class JoinReport:
    joined: List[Any]
    timestamp: str


class JoinUtils:
    @staticmethod
    def apply(left: List[Any], right: List[Any]) -> JoinReport:
        joined = list(left)
        for item in right:
            if item not in joined:
                joined.append(item)
        return JoinReport(
            joined=joined,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
