#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
circuit_utils.py — N243 Circuit Utils

Rôle :
- Fournir un outil de circuit simple
- Évaluer un chemin de valeurs
- Publier un rapport de circuit
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class CircuitReport:
    path: List[Any]
    timestamp: str


class CircuitUtils:
    @staticmethod
    def evaluate(values: List[Any], path: List[int]) -> CircuitReport:
        selected = [values[index] for index in path]
        return CircuitReport(
            path=selected,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
