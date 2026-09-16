#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
trace_utils.py — N24 N243 Trace Utils

Rôle :
- Fournir un outil simple de gestion de traces
- Publier un rapport de traces traitées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class TraceReport:
    traces: List[str]
    timestamp: str


class TraceUtils:
    @staticmethod
    def inspect(traces: List[str]) -> TraceReport:
        return TraceReport(
            traces=list(traces),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
