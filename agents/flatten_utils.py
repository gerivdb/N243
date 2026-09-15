#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
flatten_utils.py — N243 Flatten Utils

Rôle :
- Fournir un outil d'aplatissement simple
- Publier un rapport d'aplatissement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class FlattenReport:
    flat: List[Any]
    timestamp: str


class FlattenUtils:
    @staticmethod
    def apply(values: List[Any]) -> FlattenReport:
        flat: List[Any] = []
        for value in values:
            if isinstance(value, list):
                flat.extend(value)
            else:
                flat.append(value)
        return FlattenReport(
            flat=flat,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
