#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resolver_utils.py — N243 Resolver Utils

Rôle :
- Fournir un résolveur simple pour des conflits de valeurs
- Appliquer une stratégie de résolution
- Publier un rapport de résolution
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, Optional


@dataclass
class ResolveResult:
    key: str
    strategy: str
    value: Any
    timestamp: str


class ResolverUtils:
    @staticmethod
    def resolve(base: Any, override: Any, strategy: str = "override") -> Any:
        if strategy == "override":
            return override
        if strategy == "keep":
            return base
        if strategy == "merge" and isinstance(base, dict) and isinstance(override, dict):
            return {**base, **override}
        return override

    def report(self, key: str, strategy: str, value: Any) -> ResolveResult:
        return ResolveResult(
            key=key,
            strategy=strategy,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
