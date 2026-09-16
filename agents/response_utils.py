#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
response_utils.py — N24 N243 Response Utils

Rôle :
- Fournir un outil simple de gestion de réponses
- Publier un rapport de réponses générées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ResponseReport:
    responses: List[str]
    timestamp: str


class ResponseUtils:
    @staticmethod
    def inspect(responses: List[str]) -> ResponseReport:
        return ResponseReport(
            responses=list(responses),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
