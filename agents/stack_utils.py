#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
stack_utils.py — N243 Stack Utils

Rôle :
- Fournir un outil de pile simple
- Empiler des valeurs
- Publier un rapport de pile
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class StackReport:
    depth: int
    timestamp: str


class StackUtils:
    @staticmethod
    def depth(values: List[Any]) -> StackReport:
        return StackReport(
            depth=len(values),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
