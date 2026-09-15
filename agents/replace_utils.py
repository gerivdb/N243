#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
replace_utils.py — N243 Replace Utils

Rôle :
- Fournir un outil de remplacement simple
- Publier un rapport de remplacement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ReplaceReport:
    replaced: List[Any]
    timestamp: str


class ReplaceUtils:
    @staticmethod
    def apply(values: List[Any], target: Any, replacement: Any) -> ReplaceReport:
        replaced = [replacement if item == target else item for item in values]
        return ReplaceReport(
            replaced=replaced,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
