#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resolver_utils.py — N24 N243 Resolver Utils

Rôle :
- Fournir un outil simple de résolution
- Publier un rapport de résolutions effectuées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ResolveReport:
    resolved: List[str]
    timestamp: str


class ResolverUtils:
    @staticmethod
    def inspect(resolved: List[str]) -> ResolveReport:
        return ResolveReport(
            resolved=list(resolved),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
