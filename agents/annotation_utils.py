#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
annotation_utils.py — N24 N243 Annotation Utils

Rôle :
- Fournir un outil simple d'annotation
- Publier un rapport d'annotations créées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class AnnotationReport:
    annotations: List[str]
    timestamp: str


class AnnotationUtils:
    @staticmethod
    def inspect(annotations: List[str]) -> AnnotationReport:
        return AnnotationReport(
            annotations=list(annotations),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
