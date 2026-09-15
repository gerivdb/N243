#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
formatter_template_utils.py — N243 Formatter Template Utils

Rôle :
- Fournir un moteur de template simple
- Remplir des templates avec des valeurs
- Publier un rapport de rendu de template
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class TemplateReport:
    template: str
    rendered: str
    timestamp: str


class FormatterTemplateUtils:
    @staticmethod
    def render(template: str, values: Dict[str, Any]) -> str:
        result = template
        for key, value in values.items():
            result = result.replace("{" + key + "}", str(value))
        return result

    def report(self, template: str, rendered: str) -> TemplateReport:
        return TemplateReport(
            template=template,
            rendered=rendered,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
