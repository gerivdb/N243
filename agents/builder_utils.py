#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
builder_utils.py — N24 N243 Builder Utils

Rôle :
- Fournir un outil simple de construction
- Publier un rapport de builds effectués
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class BuildReport:
    builds: List[str]
    timestamp: str


class BuilderUtils:
    @staticmethod
    def inspect(builds: List[str]) -> BuildReport:
        return BuildReport(
            builds=list(builds),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
