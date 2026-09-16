#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
async_utils.py — N24 N243 Async Utils

Rôle :
- Fournir un outil simple de gestion d'opérations asynchrones
- Publier un rapport d'opérations traitées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class AsyncReport:
    operations: List[str]
    timestamp: str


class AsyncUtils:
    @staticmethod
    def inspect(operations: List[str]) -> AsyncReport:
        return AsyncReport(
            operations=list(operations),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
