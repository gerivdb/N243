#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
store_utils.py — N243 Store Utils

Rôle :
- Fournir un outil de stockage simple
- Publier un rapport de stockage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class StoreReport:
    stored: List[str]
    timestamp: str


class StoreUtils:
    @staticmethod
    def inspect(stores: List[str], payload: Dict[str, Any]) -> StoreReport:
        stored = [store for store in stores if payload.get(store) is True]
        return StoreReport(
            stored=stored,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
