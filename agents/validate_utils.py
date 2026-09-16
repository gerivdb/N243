#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_utils.py — N24 N243 Validate Utils

Rôle :
- Fournir un outil simple de validation
- Publier un rapport de validations effectuées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ValidateReport:
    valid: List[str]
    timestamp: str


class ValidateUtils:
    @staticmethod
    def inspect(valid: List[str]) -> ValidateReport:
        return ValidateReport(
            valid=list(valid),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
