#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sampler_utils.py — N243 Sampler Utils

Rôle :
- Fournir un échantillonneur simple
- Tirer un échantillon aléatoire sans remise
- Publier un rapport d'échantillonnage
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class SampleResult:
    population_size: int
    sample_size: int
    sample: List[Any]
    timestamp: str


class SamplerUtils:
    @staticmethod
    def sample(items: List[Any], size: int) -> List[Any]:
        if size > len(items):
            raise ValueError("sample size cannot exceed population size")
        return random.sample(items, size)

    def report(self, items: List[Any], size: int) -> SampleResult:
        sample = self.sample(items, size)
        return SampleResult(
            population_size=len(items),
            sample_size=len(sample),
            sample=sample,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
