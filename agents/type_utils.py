#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
type_utils.py — N243 Type Utils

Rôle :
- Fournir une introspection de types simple
- Vérifier les types (list, dict, str, int, float, bool)
- Publier un rapport de type
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class TypeReport:
    value: Any
    type_name: str
    timestamp: str


class TypeUtils:
    @staticmethod
    def is_list(value: Any) -> bool:
        return isinstance(value, list)

    @staticmethod
    def is_dict(value: Any) -> bool:
        return isinstance(value, dict)

    @staticmethod
    def is_str(value: Any) -> bool:
        return isinstance(value, str)

    @staticmethod
    def is_int(value: Any) -> bool:
        return isinstance(value, int) and not isinstance(value, bool)

    @staticmethod
    def is_float(value: Any) -> bool:
        return isinstance(value, float)

    @staticmethod
    def is_bool(value: Any) -> bool:
        return isinstance(value, bool)

    @staticmethod
    def type_name(value: Any) -> str:
        return type(value).__name__

    @staticmethod
    def report(value: Any) -> TypeReport:
        return TypeReport(
            value=value,
            type_name=TypeUtils.type_name(value),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
