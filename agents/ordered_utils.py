#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ordered_utils.py — N24 N243 Ordered Utils

Rôle :
- Fournir un outil simple de gestion d'éléments ordonnés
- Publier un rapport de collections ordonnées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class OrderedReport:
    ordered: List[str]
    timestamp: str


class OrderedUtils:
    @staticmethod
    def inspect(ordered: List[str]) -> OrderedReport:
        return OrderedReport(
            ordered=list(ordered),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
