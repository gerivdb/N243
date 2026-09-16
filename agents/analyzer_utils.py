#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analyzer_utils.py — N24 N243 Analyzer Utils

Rôle :
- Fournir un outil simple d'analyse
- Publier un rapport d'analyses effectuées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class AnalyzeReport:
    analyzed: List[str]
    timestamp: str


class AnalyzerUtils:
    @staticmethod
    def inspect(analyzed: List[str]) -> AnalyzeReport:
        return AnalyzeReport(
            analyzed=list(analyzed),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
