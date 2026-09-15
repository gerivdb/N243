#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
controller_utils.py — N243 Controller Utils

Rôle :
- Fournir un contrôleur simple
- Publier un rapport de contrôle
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ControllerReport:
    controlled: List[str]
    timestamp: str


class ControllerUtils:
    @staticmethod
    def manage(targets: List[str], payload: Dict[str, Any]) -> ControllerReport:
        controlled = [target for target in targets if payload.get(target) is True]
        return ControllerReport(
            controlled=controlled,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
