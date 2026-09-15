#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
registry.py — N243 Registry

Rôle :
- Maintenir un registre d'entrées nommées
- Ajouter, récupérer, lister
- Publier un rapport simple
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class RegistryEntry:
    name: str
    value: Any
    timestamp: str


class Registry:
    def __init__(self) -> None:
        self._entries: Dict[str, RegistryEntry] = {}

    def add(self, name: str, value: Any) -> RegistryEntry:
        entry = RegistryEntry(
            name=name,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
        self._entries[name] = entry
        return entry

    def get(self, name: str) -> Optional[RegistryEntry]:
        return self._entries.get(name)

    def list_names(self) -> List[str]:
        return list(self._entries.keys())

    def report(self) -> Dict[str, Any]:
        return {
            "count": len(self._entries),
            "entries": [
                {
                    "name": e.name,
                    "value": e.value,
                    "timestamp": e.timestamp,
                }
                for e in self._entries.values()
            ],
        }

    def to_json(self) -> str:
        return json.dumps(self.report(), ensure_ascii=False, indent=2)
