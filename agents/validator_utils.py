#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validator_utils.py — N243 Validator Utils

Rôle :
- Fournir un validateur simple de données
- Vérifier qu'un dictionnaire contient des champs requis
- Publier un rapport de validation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ValidReport:
    valid: bool
    missing: List[str]
    timestamp: str


class ValidatorUtils:
    @staticmethod
    def validate(data: Dict[str, Any], required: List[str]) -> ValidReport:
        missing = [key for key in required if key not in data]
        return ValidReport(
            valid=len(missing) == 0,
            missing=missing,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
