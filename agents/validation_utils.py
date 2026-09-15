#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validation_utils.py — N243 Validation Utils

Rôle :
- Fournir des utilitaires de validation simples
- Vérifier types, intervalles, format de chaînes
- Publier un rapport de validation
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class ValidationResult:
    valid: bool
    errors: List[str]
    checked: Dict[str, Any]
    timestamp: str


class ValidationUtils:
    def is_number(self, value: Any) -> bool:
        return isinstance(value, (int, float))

    def in_range(self, value: float, min_val: float, max_val: float) -> bool:
        return min_val <= value <= max_val

    def matches_pattern(self, text: str, pattern: str) -> bool:
        return bool(re.search(pattern, text))

    def validate(self, checks: Dict[str, Any]) -> ValidationResult:
        errors: List[str] = []
        checked: Dict[str, Any] = {}

        for name, check in checks.items():
            checked[name] = check
            if "type" in check and not self.is_number(check["value"]):
                errors.append(f"{name}: expected number, got {type(check['value']).__name__}")
            if "min" in check or "max" in check:
                if not self.is_number(check["value"]):
                    errors.append(f"{name}: cannot range-check non-number")
                else:
                    min_val = check.get("min", float("-inf"))
                    max_val = check.get("max", float("inf"))
                    if not self.in_range(check["value"], min_val, max_val):
                        errors.append(
                            f"{name}: {check['value']} not in [{min_val}, {max_val}]"
                        )
            if "pattern" in check:
                if not self.matches_pattern(str(check["value"]), check["pattern"]):
                    errors.append(f"{name}: pattern {check['pattern']} did not match")

        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
            checked=checked,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
