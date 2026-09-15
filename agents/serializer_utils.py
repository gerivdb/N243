#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
serializer_utils.py — N243 Serializer Utils

Rôle :
- Fournir un sérialiseur simple de dictionnaire
- Convertir un dictionnaire en chaîne de caractères
- Publier un rapport de sérialisation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class SerializeReport:
    length: int
    timestamp: str


class SerializerUtils:
    @staticmethod
    def to_string(data: Dict[str, Any]) -> str:
        return str(data)

    def report(self, data: Dict[str, Any]) -> SerializeReport:
        return SerializeReport(
            length=len(self.to_string(data)),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
