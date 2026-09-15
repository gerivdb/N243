#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sanitizer.py — N243 Sanitizer

Rôle :
- Nettoyer les données sensibles avant publication/stockage
- Masquer les champs sensibles connus
- Publier un rapport de sanitization
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SanitizationResult:
    original: Dict[str, Any]
    sanitized: Dict[str, Any]
    masked_fields: List[str]
    timestamp: str


class Sanitizer:
    def __init__(self, sensitive_fields: Optional[List[str]] = None) -> None:
        self.sensitive_fields = sensitive_fields or ["password", "secret", "token", "api_key"]

    def sanitize(self, data: Dict[str, Any]) -> SanitizationResult:
        sanitized = dict(data)
        masked_fields = []
        for field in self.sensitive_fields:
            if field in sanitized:
                sanitized[field] = "***"
                masked_fields.append(field)
        return SanitizationResult(
            original=data,
            sanitized=sanitized,
            masked_fields=masked_fields,
            timestamp="2026-09-15T00:00:00+00:00",
        )

    def sanitize_json(self, payload: str) -> str:
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            return payload
        result = self.sanitize(data)
        return json.dumps(result.sanitized, ensure_ascii=False)
