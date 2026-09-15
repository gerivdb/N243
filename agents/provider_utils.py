#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
provider_utils.py — N243 Provider Utils

Rôle :
- Fournir un fournisseur simple de valeurs
- Enregistrer des fournisseurs, récupérer avec fallback
- Publier un rapport de provision
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, Optional


@dataclass
class ProviderResult:
    key: str
    provided: bool
    value: Any
    timestamp: str


class ProviderUtils:
    def __init__(self) -> None:
        self._providers: Dict[str, Callable[[], Any]] = {}

    def register(self, key: str, provider: Callable[[], Any]) -> None:
        self._providers[key] = provider

    def get(self, key: str, default: Any = None) -> Any:
        provider = self._providers.get(key)
        return provider() if provider is not None else default

    def report(self, key: str, provided: bool, value: Any) -> ProviderResult:
        return ProviderResult(
            key=key,
            provided=provided,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
