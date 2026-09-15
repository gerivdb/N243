#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
composer_utils.py — N243 Composer Utils

Rôle :
- Fournir un compositeur simple d'éléments
- Joindre des éléments avec un séparateur
- Publier un rapport de composition
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class ComposeReport:
    count: int
    timestamp: str


class ComposerUtils:
    @staticmethod
    def compose(items: List[Any], separator: str = ", ") -> str:
        return separator.join(str(item) for item in items)

    def report(self, items: List[Any]) -> ComposeReport:
        return ComposeReport(
            count=len(items),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
