#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du formatter_utils.py
"""

from agents.formatter_utils import FormatterUtils, FormatterReport


class TestFormatterUtils:
    def test_format(self):
        result = FormatterUtils.format("{name} is {age}", {"name": "Alice", "age": 30})
        assert result == "Alice is 30"

    def test_interpolate(self):
        result = FormatterUtils.interpolate("{greeting}, {name}!", greeting="Hi", name="Bob")
        assert result == "Hi, Bob!"

    def test_report(self):
        r = FormatterUtils.report("{name}", {"name": "test"})
        assert r.template == "{name}"
        assert r.formatted == "test"
        assert r.timestamp
