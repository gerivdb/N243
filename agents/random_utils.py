#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
random_utils.py — N243 Random Utils

Rôle :
- Fournir une génération simple de valeurs aléatoires
- Entier, float, choix, mélange
- Publier un rapport aléatoire
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class RandomReport:
    operation: str
    value: Any
    timestamp: str


class RandomUtils:
    @staticmethod
    def int_between(min_val: int, max_val: int) -> int:
        return random.randint(min_val, max_val)

    @staticmethod
    def float_between(min_val: float, max_val: float) -> float:
        return random.uniform(min_val, max_val)

    @staticmethod
    def choice(items: List[Any]) -> Any:
        return random.choice(items)

    @staticmethod
    def shuffle(items: List[Any]) -> List[Any]:
        result = list(items)
        random.shuffle(result)
        return result

    @staticmethod
    def report(operation: str, value: Any) -> RandomReport:
        return RandomReport(
            operation=operation,
            value=value,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
