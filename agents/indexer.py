#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
indexer.py — N243 Indexer

Rôle :
- Construire des index inversés sur des collections
- Rechercher par clé d'index
- Publier un rapport d'indexation
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class IndexResult:
    key: str
    value: Any
    timestamp: str


class Indexer:
    def __init__(self) -> None:
        self.index: Dict[str, List[Any]] = {}

    def index_item(self, key: str, value: Any) -> None:
        self.index.setdefault(key, []).append(value)

    def search(self, key: str) -> List[Any]:
        return list(self.index.get(key, []))

    def report(self) -> Dict[str, Any]:
        return {
            "keys": len(self.index),
            "items": sum(len(v) for v in self.index.values()),
            "index": {k: len(v) for k, v in self.index.items()},
        }
