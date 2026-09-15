#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
identifier_utils.py — N243 Identifier Utils

Rôle :
- Fournir un générateur d'identifiants simples
- Générer des identifiants uniques préfixés
- Publier un rapport d'identification
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class IdentifierReport:
    prefix: str
    identifier: str
    timestamp: str


class IdentifierUtils:
    def __init__(self) -> None:
        self._counters: Dict[str, int] = {}

    def next(self, prefix: str) -> str:
        count = self._counters.get(prefix, 0) + 1
        self._counters[prefix] = count
        return f"{prefix}-{count:04d}"

    def report(self, prefix: str, identifier: str) -> IdentifierReport:
        return IdentifierReport(
            prefix=prefix,
            identifier=identifier,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
