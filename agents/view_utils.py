#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
view_utils.py — N243 View Utils

Rôle :
- Fournir un outil de vue simple
- Publier un rapport de vue
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ViewReport:
    rendered: List[str]
    timestamp: str


class ViewUtils:
    @staticmethod
    def render(components: List[str], payload: Dict[str, Any]) -> ViewReport:
        rendered = [component for component in components if payload.get(component) is not None]
        return ViewReport(
            rendered=rendered,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
