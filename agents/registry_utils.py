#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
registry_utils.py — N24 N243 Registry Utils

Rôle :
- Fournir un outil simple de gestion de registres
- Publier un rapport d'entrées de registre traitées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class RegistryReport:
    entries: List[str]
    timestamp: str


class RegistryUtils:
    @staticmethod
    def inspect(entries: List[str]) -> RegistryReport:
        return RegistryReport(
            entries=list(entries),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
