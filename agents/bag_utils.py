#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bag_utils.py — N24 N243 Bag Utils

Rôle :
- Fournir un outil simple de gestion de sacs
- Publier un rapport de sacs traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class BagReport:
    bags: List[str]
    timestamp: str


class BagUtils:
    @staticmethod
    def inspect(bags: List[str]) -> BagReport:
        return BagReport(
            bags=list(bags),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
