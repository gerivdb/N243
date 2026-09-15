#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_utils.py — N243 Patch Utils

Rôle :
- Fournir un outil de patch simple
- Publier un rapport de patch
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class PatchReport:
    patched: List[Any]
    timestamp: str


class PatchUtils:
    @staticmethod
    def apply(values: List[Any], index: int, replacement: Any) -> PatchReport:
        patched = list(values)
        if 0 <= index < len(patched):
            patched[index] = replacement
        return PatchReport(
            patched=patched,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
