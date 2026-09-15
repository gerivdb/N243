#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hasher_utils.py — N243 Hasher Utils

Rôle :
- Fournir un hasheur simple de texte
- Calculer un hash SHA256
- Publier un rapport de hachage
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class HashReport:
    algorithm: str
    digest: str
    timestamp: str


class HasherUtils:
    @staticmethod
    def sha256(value: str) -> str:
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    def report(self, algorithm: str, digest: str) -> HashReport:
        return HashReport(
            algorithm=algorithm,
            digest=digest,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
