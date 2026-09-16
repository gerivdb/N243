#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du weekday_utils.py
"""

from agents.weekday_utils import WeekdayUtils, WeekdayReport
from datetime import datetime


class TestWeekdayUtils:
    def test_weekday_name(self):
        dt = datetime(2024, 1, 1)  # Monday
        assert WeekdayUtils.weekday_name(dt) == "Monday"

    def test_is_weekend(self):
        dt = datetime(2024, 1, 6)  # Saturday
        assert WeekdayUtils.is_weekend(dt) is True
        assert WeekdayUtils.is_weekday(dt) is False

    def test_is_weekday(self):
        dt = datetime(2024, 1, 1)  # Monday
        assert WeekdayUtils.is_weekday(dt) is True
        assert WeekdayUtils.is_weekend(dt) is False

    def test_report(self):
        dt = datetime(2024, 1, 1)  # Monday
        r = WeekdayUtils.report(dt)
        assert r.weekday == "Monday"
        assert r.is_weekend is False
        assert r.timestamp
