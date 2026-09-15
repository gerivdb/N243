#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
builder_utils.py — N243 Builder Utils

Rôle :
- Fournir un constructeur simple pour des objets
- Construire un dictionnaire par étapes
- Publier un rapport de construction
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class BuildResult:
    steps: int
    result: Dict[str, Any]
    timestamp: str


class BuilderUtils:
    def __init__(self) -> None:
        self._data: Dict[str, Any] = {}

    def add(self, key: str, value: Any) -> None:
        self._data[key] = value

    def build(self) -> Dict[str, Any]:
        return dict(self._data)

    def report(self) -> BuildResult:
        return BuildResult(
            steps=len(self._data),
            result=dict(self._data),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
