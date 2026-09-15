#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analyzer_utils.py — N243 Analyzer Utils

Rôle :
- Fournir un analyseur simple de texte
- Calculer des statistiques basiques
- Publier un rapport d'analyse
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class AnalyzeReport:
    length: int
    words: int
    timestamp: str


class AnalyzerUtils:
    @staticmethod
    def stats(text: str) -> AnalyzeReport:
        words = text.split()
        return AnalyzeReport(
            length=len(text),
            words=len(words),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def report(self, text: str) -> AnalyzeReport:
        return self.stats(text)
