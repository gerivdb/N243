#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
process_utils.py — N24 N243 Process Utils

Rôle :
- Fournir un outil simple de gestion de processus
- Publier un rapport de processus traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class ProcessReport:
    processes: List[str]
    timestamp: str


class ProcessUtils:
    @staticmethod
    def inspect(processes: List[str]) -> ProcessReport:
        return ProcessReport(
            processes=list(processes),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
