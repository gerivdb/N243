#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
assembler_utils.py — N243 Assembler Utils

Rôle :
- Fournir un assembleur simple pour des parties
- Combiner des fragments en un tout
- Publier un rapport d'assemblage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class AssembleResult:
    parts: int
    result: Any
    timestamp: str


class AssemblerUtils:
    @staticmethod
    def assemble(parts: List[Any], joiner: str = "") -> str:
        return joiner.join(str(part) for part in parts)

    def report(self, parts: List[Any], result: Any) -> AssembleResult:
        return AssembleResult(
            parts=len(parts),
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
