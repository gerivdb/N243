#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
normalizer_utils.py — N243 Normalizer Utils

Rôle :
- Fournir une normalisation simple de texte
- Lowercase, strip, collapse espaces
- Publier un rapport de normalisation
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class NormalizerReport:
    original: str
    normalized: str
    timestamp: str


class NormalizerUtils:
    @staticmethod
    def lowercase(text: str) -> str:
        return text.lower()

    @staticmethod
    def strip(text: str) -> str:
        return text.strip()

    @staticmethod
    def collapse_spaces(text: str) -> str:
        return re.sub(r"\s+", " ", text).strip()

    @staticmethod
    def normalize(text: str) -> str:
        return NormalizerUtils.collapse_spaces(NormalizerUtils.strip(NormalizerUtils.lowercase(text)))

    @staticmethod
    def report(text: str) -> NormalizerReport:
        return NormalizerReport(
            original=text,
            normalized=NormalizerUtils.normalize(text),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
