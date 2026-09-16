#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
object_utils.py — N24 N243 Object Utils

Rôle :
- Fournir un outil simple de gestion d'objets
- Publier un rapport d'objets traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ObjectReport:
    objects: List[str]
    timestamp: str


class ObjectUtils:
    @staticmethod
    def inspect(objects: List[str]) -> ObjectReport:
        return ObjectReport(
            objects=list(objects),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
