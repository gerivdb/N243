#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validator_schema_utils.py — N243 Validator Schema Utils

Rôle :
- Fournir une validation simple de schéma
- Vérifier la présence de champs requis
- Publier un rapport de validation de schéma
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class SchemaValidationReport:
    valid: bool
    missing_fields: List[str]
    timestamp: str


class ValidatorSchemaUtils:
    @staticmethod
    def validate_fields(data: Dict[str, Any], required_fields: List[str]) -> List[str]:
        return [field for field in required_fields if field not in data]

    def report(self, data: Dict[str, Any], required_fields: List[str]) -> SchemaValidationReport:
        missing = self.validate_fields(data, required_fields)
        return SchemaValidationReport(
            valid=not missing,
            missing_fields=missing,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
