#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
date_utils.py — N243 Date Utils

Rôle :
- Fournir des utilitaires de dates simples
- Normaliser et comparer les horodatages
- Publier un rapport de date
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional


@dataclass
class DateReport:
    iso: str
    is_future: bool
    age_seconds: float
    timestamp: str


class DateUtils:
    @staticmethod
    def now_utc() -> str:
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def is_future(iso: str, reference: Optional[datetime] = None) -> bool:
        dt = datetime.fromisoformat(iso)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        ref = reference or datetime.now(timezone.utc)
        return dt > ref

    @staticmethod
    def age_seconds(iso: str, reference: Optional[datetime] = None) -> float:
        dt = datetime.fromisoformat(iso)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        ref = reference or datetime.now(timezone.utc)
        return (ref - dt).total_seconds()

    @staticmethod
    def report(iso: str) -> DateReport:
        return DateReport(
            iso=iso,
            is_future=DateUtils.is_future(iso),
            age_seconds=DateUtils.age_seconds(iso),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
