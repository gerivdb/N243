#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du math_utils.py
"""

from agents.math_utils import MathUtils, MathReport


class TestMathUtils:
    def test_clamp(self):
        assert MathUtils.clamp(5, 0, 10) == 5
        assert MathUtils.clamp(-5, 0, 10) == 0
        assert MathUtils.clamp(15, 0, 10) == 10

    def test_average(self):
        assert MathUtils.average([1.0, 2.0, 3.0]) == 2.0
        assert MathUtils.average([]) == 0.0

    def test_round_down(self):
        assert MathUtils.round_down(3.7) == 3.0
        assert MathUtils.round_down(3.789, 2) == 3.78

    def test_round_up(self):
        assert MathUtils.round_up(3.2) == 4.0
        assert MathUtils.round_up(3.211, 2) == 3.22

    def test_report(self):
        r = MathUtils.report("clamp", 5.0)
        assert r.operation == "clamp"
        assert r.value == 5.0
        assert r.timestamp
