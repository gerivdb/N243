#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zip_utils.py — N243 Zip Utils

Rôle :
- Fournir un outil de zip simple
- Publier un rapport de zip
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Tuple


@dataclass
class ZipReport:
    zipped: List[Tuple[Any, Any]]
    timestamp: str


class ZipUtils:
    @staticmethod
    def apply(left: List[Any], right: List[Any]) -> ZipReport:
        return ZipReport(
            zipped=list(zip(left, right)),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
