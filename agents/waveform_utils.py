#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
waveform_utils.py — N243 Waveform Utils

Rôle :
- Fournir un outil de forme d'onde simple
- Générer une onde sinusoïdale
- Publier un rapport de forme d'onde
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class WaveformReport:
    samples: int
    timestamp: str


class WaveformUtils:
    @staticmethod
    def sine(length: int = 10, amplitude: float = 1.0) -> List[float]:
        return [amplitude * math.sin(2 * math.pi * i / length) for i in range(length)]

    def report(self, length: int = 10) -> WaveformReport:
        return WaveformReport(
            samples=length,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
