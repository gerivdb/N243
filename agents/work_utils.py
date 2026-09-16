#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
work_utils.py — N24 N243 Work Utils

Rôle :
- Fournir un outil simple de suivi de travail
- Publier un rapport de work items traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class WorkReport:
    items: List[str]
    timestamp: str


class WorkUtils:
    @staticmethod
    def inspect(items: List[str]) -> WorkReport:
        return WorkReport(
            items=list(items),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
