#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
job_utils.py — N24 N243 Job Utils

Rôle :
- Fournir un outil simple de gestion de jobs
- Publier un rapport de jobs traités
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class JobReport:
    jobs: List[str]
    timestamp: str


class JobUtils:
    @staticmethod
    def inspect(jobs: List[str]) -> JobReport:
        return JobReport(
            jobs=list(jobs),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
