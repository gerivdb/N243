#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
flow_utils.py — N24 N243 Flow Utils

Rôle :
- Fournir un outil simple de gestion de flux
- Publier un rapport de flux traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class FlowReport:
    flows: List[str]
    timestamp: str


class FlowUtils:
    @staticmethod
    def inspect(flows: List[str]) -> FlowReport:
        return FlowReport(
            flows=list(flows),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
