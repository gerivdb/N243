#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
formatter_utils.py — N243 Formatter Utils

Rôle :
- Fournir un formatage simple de chaînes
- Interpoler des templates avec des valeurs
- Publier un rapport de formatage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class FormatterReport:
    template: str
    formatted: str
    timestamp: str


class FormatterUtils:
    @staticmethod
    def format(template: str, values: Dict[str, Any]) -> str:
        return template.format(**values)

    @staticmethod
    def interpolate(template: str, **kwargs: Any) -> str:
        return template.format(**kwargs)

    @staticmethod
    def report(template: str, values: Dict[str, Any]) -> FormatterReport:
        formatted = FormatterUtils.format(template, values)
        return FormatterReport(
            template=template,
            formatted=formatted,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
