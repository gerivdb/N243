#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du json_utils.py
"""

from agents.json_utils import JsonUtils, JsonReport


class TestJsonUtils:
    def test_loads(self):
        assert JsonUtils.loads('{"key": "value"}') == {"key": "value"}

    def test_dumps(self):
        result = JsonUtils.dumps({"key": "value"})
        assert "key" in result
        assert "value" in result

    def test_pretty(self):
        result = JsonUtils.pretty({"key": "value"})
        assert "\n" in result

    def test_report(self):
        r = JsonUtils.report({"key": "value"})
        assert r.operation == "dumps"
        assert "value" in r.result
        assert r.timestamp
