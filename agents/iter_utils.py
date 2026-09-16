#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iter_utils.py — N243 Iter Utils

Rôle :
- Fournir des utilitaires simples pour itérateurs
- Prendre, sauter, chunker des itérables
- Publier un rapport d'itération
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Iterable, List


@dataclass
class IterReport:
    operation: str
    result: List[Any]
    timestamp: str


class IterUtils:
    @staticmethod
    def take(items: Iterable[Any], count: int) -> List[Any]:
        result: List[Any] = []
        for item in items:
            if len(result) >= count:
                break
            result.append(item)
        return result

    @staticmethod
    def skip(items: Iterable[Any], count: int) -> List[Any]:
        result: List[Any] = []
        skipped = 0
        for item in items:
            if skipped < count:
                skipped += 1
                continue
            result.append(item)
        return result

    @staticmethod
    def chunk(items: Iterable[Any], size: int) -> List[List[Any]]:
        chunks: List[List[Any]] = []
        current: List[Any] = []
        for item in items:
            current.append(item)
            if len(current) >= size:
                chunks.append(current)
                current = []
        if current:
            chunks.append(current)
        return chunks

    @staticmethod
    def report(operation: str, result: List[Any]) -> IterReport:
        return IterReport(
            operation=operation,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
