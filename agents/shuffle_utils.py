#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
shuffle_utils.py — N243 Shuffle Utils

Rôle :
- Fournir un outil de mélange simple
- Publier un rapport de mélange
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ShuffleReport:
    shuffled: List[Any]
    timestamp: str


class ShuffleUtils:
    @staticmethod
    def apply(values: List[Any]) -> ShuffleReport:
        shuffled = list(values)
        random.shuffle(shuffled)
        return ShuffleReport(
            shuffled=shuffled,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
