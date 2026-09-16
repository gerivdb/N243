#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
matcher_utils.py — N243 Matcher Utils

Rôle :
- Fournir une correspondance simple de motifs
- Rechercher, trouver, remplacer des motifs
- Publier un rapport de correspondance
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class MatcherReport:
    text: str
    pattern: str
    matched: bool
    timestamp: str


class MatcherUtils:
    @staticmethod
    def matches(text: str, pattern: str) -> bool:
        return bool(re.search(pattern, text))

    @staticmethod
    def find_all(text: str, pattern: str) -> List[str]:
        return re.findall(pattern, text)

    @staticmethod
    def replace(text: str, pattern: str, replacement: str) -> str:
        return re.sub(pattern, replacement, text)

    @staticmethod
    def report(text: str, pattern: str) -> MatcherReport:
        return MatcherReport(
            text=text,
            pattern=pattern,
            matched=MatcherUtils.matches(text, pattern),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
