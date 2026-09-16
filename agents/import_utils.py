#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
import_utils.py — N24 N243 Import Utils

Rôle :
- Fournir un outil simple de gestion d'import
- Publier un rapport de fichiers importés
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ImportReport:
    imports: List[str]
    timestamp: str


class ImportUtils:
    @staticmethod
    def inspect(imports: List[str]) -> ImportReport:
        return ImportReport(
            imports=list(imports),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
