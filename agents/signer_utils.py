#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
signer_utils.py — N243 Signer Utils

Rôle :
- Fournir un signataire simple de texte
- Générer une signature basée sur un hash
- Publier un rapport de signature
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class SignReport:
    algorithm: str
    signature: str
    timestamp: str


class SignerUtils:
    @staticmethod
    def sign(value: str, secret: str) -> str:
        return hashlib.sha256(f"{value}:{secret}".encode("utf-8")).hexdigest()

    def report(self, algorithm: str, signature: str) -> SignReport:
        return SignReport(
            algorithm=algorithm,
            signature=signature,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
