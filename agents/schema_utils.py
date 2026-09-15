#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
schema_utils.py — N243 Schema Utils

Rôle :
- Fournir un outil de schéma simple
- Publier un rapport de schéma
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class SchemaReport:
    valid: List[str]
    timestamp: str


class SchemaUtils:
    @staticmethod
    def inspect(schemas: List[str], payload: Dict[str, Any]) -> SchemaReport:
        valid = [schema for schema in schemas if payload.get(schema) is True]
        return SchemaReport(
            valid=valid,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
