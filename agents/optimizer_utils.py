#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
optimizer_utils.py — N243 Optimizer Utils

Rôle :
- Fournir un optimiseur simple de calcul
- Minimiser une fonction scalaire par descente
- Publier un rapport d'optimisation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable


@dataclass
class OptimizeReport:
    iterations: int
    best_value: float
    timestamp: str


class OptimizerUtils:
    @staticmethod
    def minimize(func: Callable[[float], float], start: float, lr: float = 0.1, iterations: int = 10) -> OptimizeReport:
        x = start
        best = func(x)
        for _ in range(iterations):
            grad = (func(x + 1e-6) - func(x - 1e-6)) / 2e-6
            x -= lr * grad
            value = func(x)
            if value < best:
                best = value
        return OptimizeReport(
            iterations=iterations,
            best_value=best,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
