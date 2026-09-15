#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
io_utils.py — N243 IO Utils

Rôle :
- Fournir un outil d’entrée/sortie simple
- Publier un rapport d’E/S
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class IOReport:
    inputs: List[str]
    outputs: List[str]
    timestamp: str


class IOUtils:
    @staticmethod
    def trace(keys: List[str], payload: Dict[str, Any]) -> IOReport:
        inputs = [key for key in keys if payload.get(key) is not None]
        outputs = [key for key in keys if payload.get(key) is True]
        return IOReport(
            inputs=inputs,
            outputs=outputs,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
