#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collection_utils.py — N243 Collection Utils

Rôle :
- Fournir des utilitaires pour les collections
- Opérations courantes : dédoublonnage, tri, partition
- Publier un rapport d'opération
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Tuple


@dataclass
class CollectionResult:
    operation: str
    input_count: int
    output_count: int
    timestamp: str


class CollectionUtils:
    def deduplicate(self, items: List[Any]) -> List[Any]:
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    def partition(self, items: List[Any], predicate) -> Tuple[List[Any], List[Any]]:
        matched = []
        unmatched = []
        for item in items:
            if predicate(item):
                matched.append(item)
            else:
                unmatched.append(item)
        return matched, unmatched

    def report(self, operation: str, input_count: int, output_count: int) -> CollectionResult:
        return CollectionResult(
            operation=operation,
            input_count=input_count,
            output_count=output_count,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
