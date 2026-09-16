#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
context_utils.py — N24 N243 Context Utils

Rôle :
- Fournir un outil simple de gestion de contexte
- Publier un rapport de contextes observés
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ContextReport:
    contexts: List[str]
    timestamp: str


class ContextUtils:
    @staticmethod
    def inspect(contexts: List[str]) -> ContextReport:
        return ContextReport(
            contexts=list(contexts),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
