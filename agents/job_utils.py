#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
job_utils.py — N243 Job Utils

Rôle :
- Fournir un gestionnaire de jobs simple
- Publier un rapport de jobs
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class JobReport:
    queued: List[str]
    timestamp: str


class JobUtils:
    @staticmethod
    def queue(jobs: List[str], payload: Dict[str, Any]) -> JobReport:
        queued = [job for job in jobs if payload.get(job) is not None]
        return JobReport(
            queued=queued,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
