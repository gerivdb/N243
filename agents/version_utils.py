#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
version_utils.py — N24 N243 Version Utils

Rôle :
- Fournir un outil simple de gestion de versions
- Publier un rapport de versions détectées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class VersionReport:
    versions: List[str]
    timestamp: str


class VersionUtils:
    @staticmethod
    def inspect(versions: List[str]) -> VersionReport:
        return VersionReport(
            versions=list(versions),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
