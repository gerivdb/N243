#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unique_utils.py — N243 Unique Utils

Rôle :
- Fournir un outil d'unicité simple
- Publier un rapport d'unicité
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class UniqueReport:
    unique: List[Any]
    timestamp: str


class UniqueUtils:
    @staticmethod
    def apply(values: List[Any]) -> UniqueReport:
        unique: List[Any] = []
        for value in values:
            if value not in unique:
                unique.append(value)
        return UniqueReport(
            unique=unique,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
