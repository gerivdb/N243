#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_utils.py — N24 N243 Export Utils

Rôle :
- Fournir un outil simple de gestion d'export
- Publier un rapport de fichiers exportés
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ExportReport:
    exports: List[str]
    timestamp: str


class ExportUtils:
    @staticmethod
    def inspect(exports: List[str]) -> ExportReport:
        return ExportReport(
            exports=list(exports),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
