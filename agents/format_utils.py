#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
format_utils.py — N243 Format Utils

Rôle :
- Fournir des utilitaires de formatage simples
- Formater nombres, dates, textes
- Publier un rapport de formatage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class FormatResult:
    operation: str
    input_value: Any
    output_value: str
    timestamp: str


class FormatUtils:
    @staticmethod
    def number(value: float, digits: int = 2) -> str:
        return f"{value:.{digits}f}"

    @staticmethod
    def date(value: datetime) -> str:
        return value.strftime("%Y-%m-%d")

    @staticmethod
    def datetime(value: datetime) -> str:
        return value.strftime("%Y-%m-%d %H:%M:%S")

    def report(self, operation: str, input_value: Any, output_value: str) -> FormatResult:
        return FormatResult(
            operation=operation,
            input_value=input_value,
            output_value=output_value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
