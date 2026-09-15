#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
model_utils.py — N243 Model Utils

Rôle :
- Fournir un outil de modèle simple
- Publier un rapport de modèle
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ModelReport:
    validated: List[str]
    timestamp: str


class ModelUtils:
    @staticmethod
    def verify(models: List[str], payload: Dict[str, Any]) -> ModelReport:
        validated = [model for model in models if payload.get(model) is True]
        return ModelReport(
            validated=validated,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
