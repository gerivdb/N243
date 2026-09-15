#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
noise_utils.py — N243 Noise Utils

Rôle :
- Fournir un outil de bruit simple
- Générer du bruit aléatoire
- Publier un rapport de bruit
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class NoiseReport:
    count: int
    timestamp: str


class NoiseUtils:
    @staticmethod
    def generate(count: int = 5, minimum: float = 0.0, maximum: float = 1.0) -> List[float]:
        return [random.uniform(minimum, maximum) for _ in range(count)]

    def report(self, count: int = 5) -> NoiseReport:
        return NoiseReport(
            count=count,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
