#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du format_utils.py
"""

from datetime import datetime, timezone

from agents.format_utils import FormatUtils


class TestFormatUtils:
    def test_number(self):
        assert FormatUtils.number(3.14159, 2) == "3.14"

    def test_date(self):
        dt = datetime(2026, 1, 1, tzinfo=timezone.utc)
        assert FormatUtils.date(dt) == "2026-01-01"

    def test_datetime(self):
        dt = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
        assert FormatUtils.datetime(dt) == "2026-01-01 12:00:00"

    def test_report(self):
        utils = FormatUtils()
        result = utils.report("number", 1.5, "1.50")
        assert result.operation == "number"
        assert result.output_value == "1.50"
