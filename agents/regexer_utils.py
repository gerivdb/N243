#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
regexer_utils.py — N243 Regexer Utils

Rôle :
- Fournir un moteur de regex simple
- Rechercher un motif dans un texte
- Publier un rapport de recherche
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class RegexReport:
    pattern: str
    matches: int
    timestamp: str


class RegexerUtils:
    @staticmethod
    def search(pattern: str, text: str) -> List[str]:
        return re.findall(pattern, text)

    def report(self, pattern: str, matches: List[str]) -> RegexReport:
        return RegexReport(
            pattern=pattern,
            matches=len(matches),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
