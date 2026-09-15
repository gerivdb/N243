#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
annotation_utils.py — N243 Annotation Utils

Rôle :
- Fournir des annotations simples pour des objets
- Ajouter, lire, supprimer des annotations
- Publier un rapport d'annotation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class AnnotationResult:
    target: str
    key: str
    value: Any
    timestamp: str


class AnnotationUtils:
    def __init__(self) -> None:
        self._annotations: Dict[str, Dict[str, Any]] = {}

    def annotate(self, target: str, key: str, value: Any) -> None:
        self._annotations.setdefault(target, {})[key] = value

    def get(self, target: str, key: str, default: Any = None) -> Any:
        return self._annotations.get(target, {}).get(key, default)

    def remove(self, target: str, key: str) -> None:
        self._annotations.get(target, {}).pop(key, None)

    def keys(self, target: str) -> List[str]:
        return list(self._annotations.get(target, {}).keys())

    def report(self, target: str, key: str, value: Any) -> AnnotationResult:
        return AnnotationResult(
            target=target,
            key=key,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
