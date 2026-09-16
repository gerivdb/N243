#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
text_utils.py — N243 Text Utils

Rôle :
- Fournir des manipulations simples de texte
- Compter les mots/caractères, trouver/remplacer des motifs
- Publier un rapport de texte
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class TextReport:
    operation: str
    result: str
    timestamp: str


class TextUtils:
    @staticmethod
    def word_count(text: str) -> int:
        return len(text.split())

    @staticmethod
    def char_count(text: str) -> int:
        return len(text)

    @staticmethod
    def find_all(text: str, pattern: str) -> List[str]:
        return re.findall(pattern, text)

    @staticmethod
    def replace_all(text: str, old: str, new: str) -> str:
        return text.replace(old, new)

    @staticmethod
    def report(operation: str, result: str) -> TextReport:
        return TextReport(
            operation=operation,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
