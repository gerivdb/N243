#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mapper_utils.py — N24 N243 Mapper Utils

Rôle :
- Fournir un outil simple de mapping
- Publier un rapport de mappings créés
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class MapperReport:
    mappings: List[str]
    timestamp: str


class MapperUtils:
    @staticmethod
    def inspect(mappings: List[str]) -> MapperReport:
        return MapperReport(
            mappings=list(mappings),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
