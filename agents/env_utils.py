#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
env_utils.py — N243 Env Utils

Rôle :
- Fournir des utilitaires de variables d'environnement simples
- Lire, exiger, vérifier la présence de variables
- Publier un rapport de lecture
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional


@dataclass
class EnvReport:
    name: str
    found: bool
    value: Optional[str]
    timestamp: str


class EnvUtils:
    @staticmethod
    def get(name: str, default: Optional[str] = None) -> Optional[str]:
        return os.environ.get(name, default)

    @staticmethod
    def require(name: str) -> str:
        value = os.environ.get(name)
        if value is None:
            raise EnvironmentError(f"Missing env: {name}")
        return value

    @staticmethod
    def has(name: str) -> bool:
        return name in os.environ

    @staticmethod
    def report(name: str) -> EnvReport:
        value = os.environ.get(name)
        return EnvReport(
            name=name,
            found=value is not None,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
