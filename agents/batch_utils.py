#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
batch_utils.py — N243 Batch Utils

Rôle :
- Fournir un traitement par lots simple
- Découper des éléments en paquets
- Publier un rapport par lot
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, List


@dataclass
class BatchResult:
    batch_index: int
    batch_size: int
    result: Any
    timestamp: str


class BatchUtils:
    @staticmethod
    def batch(items: List[Any], size: int) -> List[List[Any]]:
        if size <= 0:
            raise ValueError("size must be > 0")
        return [items[i:i + size] for i in range(0, len(items), size)]

    def process(self, items: List[Any], func: Callable[[List[Any]], Any], size: int) -> List[BatchResult]:
        batches = self.batch(items, size)
        results: List[BatchResult] = []
        for index, batch in enumerate(batches, start=1):
            result = func(batch)
            results.append(
                BatchResult(
                    batch_index=index,
                    batch_size=len(batch),
                    result=result,
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
            )
        return results
