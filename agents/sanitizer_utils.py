#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sanitizer_utils.py — N243 Sanitizer Utils

Rôle :
- Fournir un assainisseur de texte simple
- Supprimer les caractères dangereux
- Publier un rapport d'assainissement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class SanitizeResult:
    original: str
    sanitized: str
    removals: int
    timestamp: str


class SanitizerUtils:
    def __init__(self, allowed_chars: str = "") -> None:
        self._allowed = set(allowed_chars)

    def sanitize(self, text: str) -> SanitizeResult:
        removals = 0
        sanitized = "".join(
            char if char.isprintable() and (not self._allowed or char in self._allowed) else ""
            for char in text
        )
        removals = len(text) - len(sanitized)
        return SanitizeResult(
            original=text,
            sanitized=sanitized,
            removals=removals,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
