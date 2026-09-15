#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
navigator_utils.py — N243 Navigator Utils

Rôle :
- Fournir un navigateur simple dans une structure
- Naviguer par chemin dans un dictionnaire
- Publier un rapport de navigation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class NavigateReport:
    path: str
    found: bool
    value: Any
    timestamp: str


class NavigatorUtils:
    @staticmethod
    def get_by_path(data: Dict[str, Any], path: str, separator: str = ".", default: Any = None) -> Any:
        keys = path.split(separator)
        current = data
        for key in keys:
            if not isinstance(current, dict) or key not in current:
                return default
            current = current[key]
        return current

    def report(self, path: str, found: bool, value: Any) -> NavigateReport:
        return NavigateReport(
            path=path,
            found=found,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
