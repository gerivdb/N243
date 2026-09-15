#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
formatter_message_utils.py — N243 Formatter Message Utils

Rôle :
- Fournir un formateur simple de messages
- Formater des messages avec des placeholders
- Publier un rapport de formatage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class FormatReport:
    template: str
    formatted: str
    timestamp: str


class FormatterMessageUtils:
    @staticmethod
    def format_message(template: str, values: Dict[str, Any]) -> str:
        result = template
        for key, value in values.items():
            result = result.replace("{" + key + "}", str(value))
        return result

    def report(self, template: str, formatted: str) -> FormatReport:
        return FormatReport(
            template=template,
            formatted=formatted,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
