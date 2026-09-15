#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mapper_utils.py — N243 Mapper Utils

Rôle :
- Fournir un mapper simple de valeurs
- Mapper des entrées vers des sorties via une table
- Publier un rapport de mapping
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class MapResult:
    input_value: Any
    output_value: Any
    mapped: bool
    timestamp: str


class MapperUtils:
    def __init__(self, mapping: Dict[Any, Any]) -> None:
        self._mapping = mapping

    def map(self, value: Any, default: Any = None) -> MapResult:
        output = self._mapping.get(value, default)
        return MapResult(
            input_value=value,
            output_value=output,
            mapped=value in self._mapping,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def keys(self) -> List[Any]:
        return list(self._mapping.keys())
