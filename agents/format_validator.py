#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
format_validator.py — N243 Format Validator

Rôle :
- Valider des formats courants (email, UUID, etc.)
- Retourner un résultat de validation structuré
- Publier un rapport de validation
"""

from __future__ import annotations

import re
import uuid
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ValidationResult:
    field_name: str
    valid: bool
    reason: str
    timestamp: str


class FormatValidator:
    def __init__(self) -> None:
        self.results: List[ValidationResult] = []

    def validate_email(self, field_name: str, value: str) -> ValidationResult:
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        valid = bool(re.match(pattern, value))
        reason = "valid" if valid else "invalid email format"
        result = ValidationResult(field_name=field_name, valid=valid, reason=reason, timestamp="2026-09-15T00:00:00+00:00")
        self.results.append(result)
        return result

    def validate_uuid(self, field_name: str, value: str) -> ValidationResult:
        try:
            uuid.UUID(value)
            valid = True
            reason = "valid"
        except (ValueError, AttributeError):
            valid = False
            reason = "invalid uuid format"
        result = ValidationResult(field_name=field_name, valid=valid, reason=reason, timestamp="2026-09-15T00:00:00+00:00")
        self.results.append(result)
        return result

    def validate_regex(self, field_name: str, value: str, pattern: str) -> ValidationResult:
        valid = bool(re.match(pattern, value))
        reason = "valid" if valid else "invalid format"
        result = ValidationResult(field_name=field_name, valid=valid, reason=reason, timestamp="2026-09-15T00:00:00+00:00")
        self.results.append(result)
        return result

    def report(self) -> Dict[str, Any]:
        return {
            "total": len(self.results),
            "valid": sum(1 for r in self.results if r.valid),
            "invalid": sum(1 for r in self.results if not r.valid),
            "results": [
                {
                    "field_name": r.field_name,
                    "valid": r.valid,
                    "reason": r.reason,
                    "timestamp": r.timestamp,
                }
                for r in self.results
            ],
        }
