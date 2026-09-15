#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timezone_utils.py — N243 Timezone Utils

Rôle :
- Convertir des horodatages entre fuseaux horaires
- Normaliser les dates en UTC
- Publier un rapport de conversion
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Optional


@dataclass
class TimezoneResult:
    original: str
    converted: str
    from_tz: str
    to_tz: str
    timestamp: str


class TimezoneUtils:
    def to_utc(self, iso: str, from_tz: Optional[timezone] = None) -> str:
        dt = datetime.fromisoformat(iso)
        if from_tz is not None:
            dt = dt.replace(tzinfo=from_tz)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).isoformat()

    def convert(self, iso: str, from_tz: Optional[timezone], to_tz: timezone) -> TimezoneResult:
        converted = self.to_utc(iso, from_tz)
        dt = datetime.fromisoformat(converted)
        converted = dt.astimezone(to_tz).isoformat()
        return TimezoneResult(
            original=iso,
            converted=converted,
            from_tz=from_tz.tzname(None) if from_tz else "UTC",
            to_tz=to_tz.tzname(None),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
