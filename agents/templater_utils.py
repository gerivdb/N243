#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
templater_utils.py — N243 Templater Utils

Rôle :
- Fournir un moteur de template simple
- Remplir un template avec des variables
- Publier un rapport de templating
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class TemplateReport:
    template_length: int
    rendered_length: int
    timestamp: str


class TemplaterUtils:
    @staticmethod
    def render(template: str, variables: Dict[str, Any]) -> str:
        result = template
        for key, value in variables.items():
            result = result.replace(f"{{{{{key}}}}}", str(value))
        return result

    def report(self, template: str, rendered: str) -> TemplateReport:
        return TemplateReport(
            template_length=len(template),
            rendered_length=len(rendered),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
