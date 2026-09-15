#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du timezone_utils.py
"""

from datetime import timezone, timedelta
from agents.timezone_utils import TimezoneUtils


class TestTimezoneUtils:
    def test_to_utc(self):
        utils = TimezoneUtils()
        iso = "2026-09-15T12:00:00+02:00"
        assert utils.to_utc(iso) == "2026-09-15T10:00:00+00:00"

    def test_convert(self):
        utils = TimezoneUtils()
        from_tz = timezone(timedelta(hours=2))
        to_tz = timezone.utc
        result = utils.convert("2026-09-15T12:00:00", from_tz, to_tz)
        assert result.converted == "2026-09-15T10:00:00+00:00"
        assert result.from_tz == "UTC+02:00"
