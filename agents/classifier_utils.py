#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
classifier_utils.py — N243 Classifier Utils

Rôle :
- Fournir un classificateur simple par règles
- Classifier des valeurs selon des critères
- Publier un rapport de classification
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass
class ClassificationResult:
    value: Any
    label: str
    score: float
    timestamp: str


class ClassifierUtils:
    def __init__(self, rules: Dict[str, Callable[[Any], bool]]) -> None:
        self._rules = rules

    def classify(self, value: Any) -> ClassificationResult:
        for label, rule in self._rules.items():
            if rule(value):
                return ClassificationResult(
                    value=value,
                    label=label,
                    score=1.0,
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
        return ClassificationResult(
            value=value,
            label="unknown",
            score=0.0,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
