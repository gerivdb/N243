#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mapper.py — N243 Mapper

Rôle :
- Transformer des données d'un format à un autre
- Appliquer des mappings prédéfinis
- Publier un rapport de mapping
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class MapResult:
    source: Dict[str, Any]
    target: Dict[str, Any]
    mapped_fields: List[str]
    skipped_fields: List[str]
    timestamp: str


class Mapper:
    def __init__(self, field_map: Optional[Dict[str, str]] = None) -> None:
        self.field_map = field_map or {}

    def map(self, source: Dict[str, Any]) -> MapResult:
        target: Dict[str, Any] = {}
        mapped_fields = []
        skipped_fields = []
        for src_key, dst_key in self.field_map.items():
            if src_key in source:
                target[dst_key] = source[src_key]
                mapped_fields.append(dst_key)
            else:
                skipped_fields.append(src_key)
        return MapResult(
            source=source,
            target=target,
            mapped_fields=mapped_fields,
            skipped_fields=skipped_fields,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def report(self) -> Dict[str, Any]:
        return {
            "field_map": self.field_map,
            "mappings": len(self.field_map),
        }
