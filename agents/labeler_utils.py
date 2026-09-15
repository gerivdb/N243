#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
labeler_utils.py — N243 Labeler Utils

Rôle :
- Fournir un étiqueteur simple d'éléments
- Attacher des étiquettes à des éléments
- Publier un rapport d'étiquetage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class LabelReport:
    labeled: int
    labels: List[str]
    timestamp: str


class LabelerUtils:
    def __init__(self) -> None:
        self._labels: Dict[Any, List[str]] = {}

    def label(self, item: Any, label: str) -> None:
        self._labels.setdefault(item, []).append(label)

    def labels_for(self, item: Any) -> List[str]:
        return list(self._labels.get(item, []))

    def report(self) -> LabelReport:
        all_labels = sorted({label for labels in self._labels.values() for label in labels})
        return LabelReport(
            labeled=len(self._labels),
            labels=all_labels,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
