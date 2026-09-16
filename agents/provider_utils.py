#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
provider_utils.py — N243 Provider Utils

Rôle :
- Fournir un outil de fournisseur simple
- Publier un rapport de fournisseur
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ProviderReport:
    provided: List[str]
    timestamp: str


class ProviderUtils:
    @staticmethod
    def inspect(providers: List[str], payload: Dict[str, Any]) -> ProviderReport:
        provided = [provider for provider in providers if payload.get(provider) is True]
        return ProviderReport(
            provided=provided,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
