#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
classifier_utils.py — N24 N243 Classifier Utils

Rôle :
- Fournir un outil simple de classification
- Publier un rapport de classifications effectuées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ClassifyReport:
    classes: List[str]
    timestamp: str


class ClassifierUtils:
    @staticmethod
    def inspect(classes: List[str]) -> ClassifyReport:
        return ClassifyReport(
            classes=list(classes),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
