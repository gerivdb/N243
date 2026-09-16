#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
file_utils.py — N24 N243 File Utils

Rôle :
- Fournir un outil simple de gestion de fichiers
- Publier un rapport de fichiers traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class FileReport:
    files: List[str]
    timestamp: str


class FileUtils:
    @staticmethod
    def inspect(files: List[str]) -> FileReport:
        return FileReport(
            files=list(files),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
