#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
config_utils.py — N24 N243 Config Utils

Rôle :
- Fournir un outil simple de gestion de configuration
- Publier un rapport de configs traitées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class ConfigReport:
    configs: Dict[str, Any]
    timestamp: str


class ConfigUtils:
    @staticmethod
    def inspect(configs: Dict[str, Any]) -> ConfigReport:
        return ConfigReport(
            configs=dict(configs),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
