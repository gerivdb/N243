#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du round_utils.py
"""

from agents.round_utils import RoundUtils, RoundReport


class TestRoundUtils:
    def test_round_half_up(self):
        assert RoundUtils.round_half_up(2.5) == 3.0
        assert RoundUtils.round_half_up(2.4) == 2.0
        assert RoundUtils.round_half_up(2.456, 2) == 2.46

    def test_floor(self):
        assert RoundUtils.floor(3.7) == 3.0
        assert RoundUtils.floor(3.789, 2) == 3.78

    def test_ceil(self):
        assert RoundUtils.ceil(3.2) == 4.0
        assert RoundUtils.ceil(3.211, 2) == 3.22

    def test_report(self):
        r = RoundUtils.report("round_half_up", 2.5)
        assert r.operation == "round_half_up"
        assert r.value == 2.5
        assert r.timestamp
