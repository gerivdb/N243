#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rollback_utils.py — N243 Rollback Utils

Rôle :
- Fournir un outil de retour simple
- Publier un rapport de retour
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class RollbackReport:
    rolled_back: List[Any]
    timestamp: str


class RollbackUtils:
    @staticmethod
    def filter(payloads: List[Dict[str, Any]]) -> RollbackReport:
        rolled_back = [payload.get("value") for payload in payloads if payload.get("rollback", False)]
        return RollbackReport(
            rolled_back=rolled_back,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
