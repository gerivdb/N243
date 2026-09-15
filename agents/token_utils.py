#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
token_utils.py — N243 Token Utils

Rôle :
- Fournir des utilitaires de tokenisation simple
- Découper un texte en tokens
- Publier un rapport de tokenisation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class TokenResult:
    token_count: int
    tokens: List[str]
    timestamp: str


class TokenUtils:
    @staticmethod
    def tokenize(text: str, sep: str = " ") -> List[str]:
        if not text:
            return []
        return text.split(sep)

    def report(self, text: str, sep: str = " ") -> TokenResult:
        tokens = self.tokenize(text, sep)
        return TokenResult(
            token_count=len(tokens),
            tokens=tokens,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
