#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
object_utils.py — N243 Object Utils

Rôle :
- Fournir des utilitaires pour les objets/dicts
- Deep get/set limité
- Publier un rapport simple
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class ObjectResult:
    operation: str
    path: str
    value: Any
    timestamp: str


class ObjectUtils:
    def get(self, data: Dict[str, Any], path: str) -> Any:
        keys = path.split(".")
        current = data
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current

    def set(self, data: Dict[str, Any], path: str, value: Any) -> None:
        keys = path.split(".")
        current = data
        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value

    def report(self, operation: str, path: str, value: Any) -> ObjectResult:
        return ObjectResult(
            operation=operation,
            path=path,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
