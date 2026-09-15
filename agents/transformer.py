#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transformer.py — N243 Transformer

Rôle :
- Transformer des données avec des fonctions applicatives
- Empiler des transformations
- Publier un rapport de transformation
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional


@dataclass
class TransformResult:
    original: Any
    transformed: Any
    transformation: str
    timestamp: str


class Transformer:
    def __init__(self) -> None:
        self.results: List[TransformResult] = []

    def apply(self, value: Any, transformation: str, func: Callable[[Any], Any]) -> Any:
        transformed = func(value)
        self.results.append(TransformResult(
            original=value,
            transformed=transformed,
            transformation=transformation,
            timestamp=datetime.now(timezone.utc).isoformat(),
        ))
        return transformed

    def report(self) -> Dict[str, Any]:
        return {
            "total": len(self.results),
            "results": [
                {
                    "transformation": r.transformation,
                    "original": r.original,
                    "transformed": r.transformed,
                    "timestamp": r.timestamp,
                }
                for r in self.results
            ],
        }

    def to_json(self) -> str:
        return json.dumps(self.report(), ensure_ascii=False, indent=2)
