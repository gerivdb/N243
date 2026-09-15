#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
window_utils.py — N243 Window Utils

Rôle :
- Fournir un outil de fenêtrage simple
- Publier un rapport de fenêtrage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class WindowReport:
    windows: List[List[Any]]
    timestamp: str


class WindowUtils:
    @staticmethod
    def apply(values: List[Any], size: int) -> WindowReport:
        windows = [values[index:index + size] for index in range(len(values) - size + 1)]
        return WindowReport(
            windows=windows,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
