#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
serializer.py — N243 Serializer

Rôle :
- Sérialiser/déserialiser des données en JSON/YAML
- Garantir la compatibilité des formats
- Publier un rapport de sérialisation
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, Optional


@dataclass
class SerializeResult:
    format: str
    success: bool
    data: str
    timestamp: str


class Serializer:
    def to_json(self, data: Dict[str, Any]) -> SerializeResult:
        try:
            payload = json.dumps(data, ensure_ascii=False, indent=2)
            return SerializeResult(
                format="json",
                success=True,
                data=payload,
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
        except (TypeError, ValueError) as e:
            return SerializeResult(
                format="json",
                success=False,
                data=str(e),
                timestamp=datetime.now(timezone.utc).isoformat(),
            )

    def from_json(self, payload: str) -> SerializeResult:
        try:
            data = json.loads(payload)
            return SerializeResult(
                format="json",
                success=True,
                data=json.dumps(data, ensure_ascii=False, indent=2),
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            return SerializeResult(
                format="json",
                success=False,
                data=str(e),
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
