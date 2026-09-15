#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
policy_utils.py — N243 Policy Utils

Rôle :
- Fournir un outil de politique simple
- Publier un rapport de politique
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class PolicyReport:
    applied: List[str]
    timestamp: str


class PolicyUtils:
    @staticmethod
    def enforce(rules: List[str], payload: Dict[str, Any]) -> PolicyReport:
        applied = [rule for rule in rules if payload.get(rule) is True]
        return PolicyReport(
            applied=applied,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
