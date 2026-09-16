#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du time_utils.py
"""

from agents.time_utils import TimeUtils, TimeReport
from datetime import datetime, timezone


class TestTimeUtils:
    def test_now_utc(self):
        result = TimeUtils.now_utc()
        assert result.tzinfo is not None

    def test_isoformat(self):
        dt = datetime(2024, 1, 1, tzinfo=timezone.utc)
        assert TimeUtils.isoformat(dt) == "2024-01-01T00:00:00+00:00"

    def test_format_hhmmss(self):
        dt = datetime(2024, 1, 1, 14, 30, 45, tzinfo=timezone.utc)
        assert TimeUtils.format_hhmmss(dt) == "14:30:45"

    def test_report(self):
        r = TimeUtils.report("now_utc", TimeUtils.isoformat())
        assert r.operation == "now_utc"
        assert r.timestamp
