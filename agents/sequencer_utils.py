#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sequencer_utils.py — N243 Sequencer Utils

Rôle :
- Fournir un séquenceur simple d'étapes
- Exécuter des étapes dans l'ordre
- Publier un rapport par étape
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, List


@dataclass
class SequenceReport:
    step: int
    status: str
    result: Any
    error: str
    timestamp: str


class SequencerUtils:
    def __init__(self, steps: List[Callable[[], Any]]) -> None:
        self._steps = steps

    def run(self) -> List[SequenceReport]:
        reports: List[SequenceReport] = []
        for index, step in enumerate(self._steps, start=1):
            try:
                result = step()
                report = SequenceReport(
                    step=index,
                    status="ok",
                    result=result,
                    error="",
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
            except Exception as exc:  # noqa: BLE001
                report = SequenceReport(
                    step=index,
                    status="error",
                    result=None,
                    error=str(exc),
                    timestamp=datetime.now(timezone.utc).isoformat(),
                )
            reports.append(report)
            if report.status == "error":
                break
        return reports
