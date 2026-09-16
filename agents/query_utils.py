#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
query_utils.py — N24 N243 Query Utils

Rôle :
- Fournir un outil simple de gestion de requêtes
- Publier un rapport de requêtes traitées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class QueryReport:
    queries: List[str]
    timestamp: str


class QueryUtils:
    @staticmethod
    def inspect(queries: List[str]) -> QueryReport:
        return QueryReport(
            queries=list(queries),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
