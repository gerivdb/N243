#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
json_utils.py — N243 JSON Utils

Rôle :
- Fournir des utilitaires simples de manipulation de JSON
- Charger, sérialiser, formater du JSON
- Publier un rapport de sérialisation
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Optional


@dataclass
class JsonReport:
    operation: str
    result: str
    timestamp: str


class JsonUtils:
    @staticmethod
    def loads(text: str) -> Any:
        return json.loads(text)

    @staticmethod
    def dumps(value: Any, indent: Optional[int] = None) -> str:
        return json.dumps(value, indent=indent, ensure_ascii=False)

    @staticmethod
    def pretty(value: Any) -> str:
        return JsonUtils.dumps(value, indent=2)

    @staticmethod
    def report(value: Any) -> JsonReport:
        return JsonReport(
            operation="dumps",
            result=JsonUtils.dumps(value),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
