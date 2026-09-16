#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du number_utils.py
"""

from agents.number_utils import NumberUtils, NumberReport


class TestNumberUtils:
    def test_clamp(self):
        assert NumberUtils.clamp(5, 0, 10) == 5
        assert NumberUtils.clamp(-5, 0, 10) == 0
        assert NumberUtils.clamp(15, 0, 10) == 10

    def test_average(self):
        assert NumberUtils.average([1.0, 2.0, 3.0]) == 2.0
        assert NumberUtils.average([]) == 0.0

    def test_normalize(self):
        assert NumberUtils.normalize(5, 0, 10) == 0.5
        assert NumberUtils.normalize(5, 5, 5) == 0.0

    def test_report(self):
        r = NumberUtils.report("clamp", 5.0)
        assert r.operation == "clamp"
        assert r.value == 5.0
        assert r.timestamp
