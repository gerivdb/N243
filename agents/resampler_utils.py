#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resampler_utils.py — N243 Resampler Utils

Rôle :
- Fournir un outil de rééchantillonnage simple
- Sélectionner un sous-ensemble régulier d'éléments
- Publier un rapport de rééchantillonnage
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, List


@dataclass
class ResampleReport:
    original_count: int
    resampled_count: int
    timestamp: str


class ResamplerUtils:
    @staticmethod
    def downsample(values: List[Any], step: int = 2) -> List[Any]:
        return values[::step]

    def report(self, values: List[Any], step: int = 2) -> ResampleReport:
        return ResampleReport(
            original_count=len(values),
            resampled_count=len(self.downsample(values, step)),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
