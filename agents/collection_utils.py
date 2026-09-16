#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collection_utils.py — N24 N243 Collection Utils

Rôle :
- Fournir un outil simple de gestion de collections
- Publier un rapport de collections traitées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class CollectionReport:
    collections: List[str]
    timestamp: str


class CollectionUtils:
    @staticmethod
    def inspect(collections: List[str]) -> CollectionReport:
        return CollectionReport(
            collections=list(collections),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
