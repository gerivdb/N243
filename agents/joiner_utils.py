#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
joiner_utils.py — N243 Joiner Utils

Rôle :
- Fournir un joineur simple de collections
- Joindre des listes ou des chaînes
- Publier un rapport de jointure
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class JoinReport:
    separator: str
    result: str
    timestamp: str


class JoinerUtils:
    @staticmethod
    def join(values: List[Any], separator: str = "") -> str:
        return separator.join(str(value) for value in values)

    def report(self, separator: str, result: str) -> JoinReport:
        return JoinReport(
            separator=separator,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
