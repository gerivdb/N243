#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
string_utils.py — N243 String Utils

Rôle :
- Fournir des manipulations de chaînes simples
- slugify, truncate, split_preserve
- Publier un rapport de chaîne
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List, Optional


@dataclass
class StringReport:
    operation: str
    result: str
    timestamp: str


class StringUtils:
    @staticmethod
    def slugify(text: str) -> str:
        text = text.lower().strip()
        text = re.sub(r"[^a-z0-9]+", "-", text)
        return text.strip("-")

    @staticmethod
    def truncate(text: str, max_length: int, suffix: str = "...") -> str:
        if len(text) <= max_length:
            return text
        return text[: max_length - len(suffix)] + suffix

    @staticmethod
    def split_preserve(text: str, sep: str) -> List[str]:
        if not text:
            return []
        return text.split(sep)

    @staticmethod
    def report(operation: str, result: str) -> StringReport:
        return StringReport(
            operation=operation,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
