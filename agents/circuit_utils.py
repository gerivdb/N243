#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
circuit_utils.py — N24 N243 Circuit Utils

Rôle :
- Fournir un outil simple de gestion de circuits
- Publier un rapport de circuits traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class CircuitReport:
    circuits: List[str]
    timestamp: str


class CircuitUtils:
    @staticmethod
    def inspect(circuits: List[str]) -> CircuitReport:
        return CircuitReport(
            circuits=list(circuits),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
