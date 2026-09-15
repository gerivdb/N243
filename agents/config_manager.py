#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
config_manager.py — N243 Config Manager

Rôle :
- Gérer les configurations par environnement
- Fournir des valeurs par défaut
- Publier un rapport de configuration
"""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, Optional


@dataclass
class Config:
    environment: str
    values: Dict[str, Any]
    timestamp: str


class ConfigManager:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self.defaults = defaults or {}
        self.configs: Dict[str, Config] = {}

    def add_environment(self, name: str, values: Dict[str, Any]) -> None:
        self.configs[name] = Config(
            environment=name,
            values=values,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def get(self, environment: str, key: str, default: Any = None) -> Any:
        env = self.configs.get(environment)
        if env is None:
            return self.defaults.get(key, default)
        return env.values.get(key, self.defaults.get(key, default))

    def report(self) -> Dict[str, Any]:
        return {
            "environments": list(self.configs.keys()),
            "defaults": self.defaults,
            "configs": [
                {
                    "environment": c.environment,
                    "values": c.values,
                    "timestamp": c.timestamp,
                }
                for c in self.configs.values()
            ],
        }

    def to_json(self) -> str:
        return json.dumps(self.report(), ensure_ascii=False, indent=2)
