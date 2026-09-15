#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sanitizer_utils.py — N243 Sanitizer Utils

Rôle :
- Fournir un assainisseur simple de chaînes
- Supprimer des caractères indésirables
- Publier un rapport d'assainissement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class SanitizeReport:
    original: str
    sanitized: str
    removed: int
    timestamp: str


class SanitizerUtils:
    @staticmethod
    def remove_chars(value: str, chars: List[str]) -> str:
        for char in chars:
            value = value.replace(char, "")
        return value

    def report(self, original: str, sanitized: str, removed: int) -> SanitizeReport:
        return SanitizeReport(
            original=original,
            sanitized=sanitized,
            removed=removed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
