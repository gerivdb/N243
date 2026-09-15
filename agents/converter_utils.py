#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
converter_utils.py — N243 Converter Utils

Rôle :
- Fournir un convertisseur simple pour des types
- Convertir des chaînes vers des types courants
- Publier un rapport de conversion
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ConvertResult:
    source_type: str
    target_type: str
    success: bool
    value: Any
    timestamp: str


class ConverterUtils:
    @staticmethod
    def to_int(value: str, default: int = 0) -> int:
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    @staticmethod
    def to_float(value: str, default: float = 0.0) -> float:
        try:
            return float(value)
        except (TypeError, ValueError):
            return default

    @staticmethod
    def to_bool(value: str, default: bool = False) -> bool:
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.strip().lower() in ("true", "1", "yes", "on")
        return default

    def report(self, source_type: str, target_type: str, success: bool, value: Any) -> ConvertResult:
        return ConvertResult(
            source_type=source_type,
            target_type=target_type,
            success=success,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
