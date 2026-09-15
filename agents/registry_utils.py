#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
registry_utils.py — N243 Registry Utils

Rôle :
- Fournir un registre simple par nom
- Ajouter, récupérer, lister, supprimer des éléments
- Publier un rapport d'état du registre
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class RegistryResult:
    operation: str
    name: str
    status: str
    timestamp: str


class RegistryUtils:
    def __init__(self) -> None:
        self._items: Dict[str, Any] = {}

    def add(self, name: str, value: Any) -> None:
        self._items[name] = value

    def get(self, name: str, default: Any = None) -> Any:
        return self._items.get(name, default)

    def remove(self, name: str) -> None:
        self._items.pop(name, None)

    def list_items(self) -> List[str]:
        return list(self._items.keys())

    def has(self, name: str) -> bool:
        return name in self._items

    def report(self, operation: str, name: str, status: str) -> RegistryResult:
        return RegistryResult(
            operation=operation,
            name=name,
            status=status,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
