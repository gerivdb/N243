#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
error_utils.py — N243 Error Utils

Rôle :
- Fournir un outil d’erreur simple
- Publier un rapport d’erreur
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ErrorReport:
    errors: List[str]
    timestamp: str


class ErrorUtils:
    @staticmethod
    def collect(errors: List[str], payload: Dict[str, Any]) -> ErrorReport:
        collected = [error for error in errors if payload.get(error) is True]
        return ErrorReport(
            errors=collected,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
