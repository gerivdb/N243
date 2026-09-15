#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rule_utils.py — N243 Rule Utils

Rôle :
- Fournir un outil de règle simple
- Publier un rapport de règle
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class RuleReport:
    matched: List[str]
    timestamp: str


class RuleUtils:
    @staticmethod
    def evaluate(rules: List[str], payload: Dict[str, Any]) -> RuleReport:
        matched = [rule for rule in rules if payload.get(rule) is True]
        return RuleReport(
            matched=matched,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
