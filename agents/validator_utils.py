#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validator_utils.py — N243 Validator Utils

Rôle :
- Fournir un validateur simple pour des entrées
- Valider présence, type, bornes
- Publier un rapport de validation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class ValidationResult:
    valid: bool
    errors: List[str]
    timestamp: str


class ValidatorUtils:
    def required(self, name: str, value: Any) -> Optional[str]:
        if value is None:
            return f"{name} is required"
        return None

    def type_check(self, name: str, value: Any, expected_type: type) -> Optional[str]:
        if not isinstance(value, expected_type):
            return f"{name} expected {expected_type.__name__}, got {type(value).__name__}"
        return None

    def range_check(self, name: str, value: float, min_val: float, max_val: float) -> Optional[str]:
        if not (min_val <= value <= max_val):
            return f"{name} {value} not in [{min_val}, {max_val}]"
        return None

    def validate(self, checks: List[Dict[str, Any]]) -> ValidationResult:
        errors: List[str] = []
        for check in checks:
            name = check["name"]
            value = check.get("value")
            if "required" in check and check["required"]:
                error = self.required(name, value)
                if error:
                    errors.append(error)
            if "type" in check:
                error = self.type_check(name, value, check["type"])
                if error:
                    errors.append(error)
            if "min" in check and "max" in check and isinstance(value, (int, float)):
                error = self.range_check(name, value, check["min"], check["max"])
                if error:
                    errors.append(error)

        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
