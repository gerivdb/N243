#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sampler.py — N243 Sampler

Rôle :
- Échantillonner des éléments d'une collection
- Calculer des statistiques simples sur l'échantillon
- Publier un rapport d'échantillonnage
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class SampleResult:
    sample_size: int
    population_size: int
    items: List[Any]
    timestamp: str


class Sampler:
    def __init__(self, seed: Optional[int] = None) -> None:
        self.rng = random.Random(seed)

    def sample(self, items: List[Any], size: int) -> SampleResult:
        population_size = len(items)
        sample_size = min(size, population_size)
        sampled = self.rng.sample(items, sample_size)
        return SampleResult(
            sample_size=sample_size,
            population_size=population_size,
            items=sampled,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def report(self, result: SampleResult) -> Dict[str, Any]:
        return {
            "sample_size": result.sample_size,
            "population_size": result.population_size,
            "ratio": result.sample_size / result.population_size if result.population_size else 0.0,
        }
