#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cipher_utils.py — N24 N243 Cipher Utils

Rôle :
- Fournir un outil simple de gestion de chiffrement
- Publier un rapport de chiffrements effectués
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class CipherReport:
    encrypts: List[str]
    timestamp: str


class CipherUtils:
    @staticmethod
    def inspect(encrypts: List[str]) -> CipherReport:
        return CipherReport(
            encrypts=list(encrypts),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
