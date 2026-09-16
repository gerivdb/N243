#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
weekday_utils.py — N243 Weekday Utils

Rôle :
- Fournir des utilitaires simples pour les jours de la semaine
- weekday_name, is_weekend, is_weekday
- Publier un rapport de jour de la semaine
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class WeekdayReport:
    date_str: str
    weekday: str
    is_weekend: bool
    timestamp: str


class WeekdayUtils:
    @staticmethod
    def weekday_name(date: Optional[datetime] = None) -> str:
        if date is None:
            date = datetime.now()
        return date.strftime("%A")

    @staticmethod
    def is_weekend(date: Optional[datetime] = None) -> bool:
        if date is None:
            date = datetime.now()
        return date.weekday() >= 5

    @staticmethod
    def is_weekday(date: Optional[datetime] = None) -> bool:
        return not WeekdayUtils.is_weekend(date)

    @staticmethod
    def report(date: Optional[datetime] = None) -> WeekdayReport:
        if date is None:
            date = datetime.now()
        return WeekdayReport(
            date_str=date.isoformat(),
            weekday=WeekdayUtils.weekday_name(date),
            is_weekend=WeekdayUtils.is_weekend(date),
            timestamp=datetime.now().isoformat(),
        )
