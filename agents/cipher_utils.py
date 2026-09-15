#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cipher_utils.py — N243 Cipher Utils

Rôle :
- Fournir un chiffreur simple de texte
- Appliquer un chiffrement par décalage
- Publier un rapport de chiffrement
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class CipherReport:
    algorithm: str
    encrypted: str
    timestamp: str


class CipherUtils:
    @staticmethod
    def caesar(value: str, shift: int = 3) -> str:
        result = []
        for char in value:
            if char.isalpha():
                base = 65 if char.isupper() else 97
                result.append(chr((ord(char) - base + shift) % 26 + base))
            else:
                result.append(char)
        return "".join(result)

    def report(self, algorithm: str, encrypted: str) -> CipherReport:
        return CipherReport(
            algorithm=algorithm,
            encrypted=encrypted,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
