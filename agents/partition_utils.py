#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
partition_utils.py — N243 Partition Utils

Rôle :
- Fournir un outil de partition simple
- Publier un rapport de partition
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class PartitionReport:
    truthy: List[Any]
    falsy: List[Any]
    timestamp: str


class PartitionUtils:
    @staticmethod
    def apply(values: List[Any]) -> PartitionReport:
        truthy: List[Any] = []
        falsy: List[Any] = []
        for value in values:
            if value:
                truthy.append(value)
            else:
                falsy.append(value)
        return PartitionReport(
            truthy=truthy,
            falsy=falsy,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
