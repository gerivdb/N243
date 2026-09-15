#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
supplier_utils.py — N243 Supplier Utils

Rôle :
- Fournir un fournisseur avec cache simple
- Enregistrer des fournisseurs, récupérer avec fallback
- Publier un rapport de fourniture
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, Optional


@dataclass
class SupplierResult:
    key: str
    cached: bool
    value: Any
    timestamp: str


class SupplierUtils:
    def __init__(self) -> None:
        self._cache: Dict[str, Any] = {}
        self._providers: Dict[str, Callable[[], Any]] = {}

    def register(self, key: str, provider: Callable[[], Any]) -> None:
        self._providers[key] = provider

    def get(self, key: str, default: Any = None) -> Any:
        if key in self._cache:
            return self._cache[key]
        provider = self._providers.get(key)
        if provider is not None:
            value = provider()
            self._cache[key] = value
            return value
        return default

    def report(self, key: str, cached: bool, value: Any) -> SupplierResult:
        return SupplierResult(
            key=key,
            cached=cached,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
