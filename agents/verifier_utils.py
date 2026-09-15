#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifier_utils.py — N243 Verifier Utils

Rôle :
- Fournir un vérificateur simple de signature
- Vérifier une signature SHA256
- Publier un rapport de vérification
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class VerifyReport:
    algorithm: str
    valid: bool
    timestamp: str


class VerifierUtils:
    @staticmethod
    def verify(value: str, secret: str, expected: str) -> bool:
        return hashlib.sha256(f"{value}:{secret}".encode("utf-8")).hexdigest() == expected

    def report(self, algorithm: str, valid: bool) -> VerifyReport:
        return VerifyReport(
            algorithm=algorithm,
            valid=valid,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
