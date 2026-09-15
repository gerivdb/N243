#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deserializer_utils.py — N243 Deserializer Utils

Rôle :
- Fournir un désérialiseur simple de chaîne de caractères
- Convertir une chaîne représentant un dictionnaire en dictionnaire
- Publier un rapport de désérialisation
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class DeserializeReport:
    success: bool
    timestamp: str


class DeserializerUtils:
    @staticmethod
    def from_string(value: str) -> Dict[str, Any]:
        return ast.literal_eval(value)

    def report(self, success: bool) -> DeserializeReport:
        return DeserializeReport(
            success=success,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
