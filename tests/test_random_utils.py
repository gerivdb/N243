#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du random_utils.py
"""

from agents.random_utils import RandomUtils, RandomReport


class TestRandomUtils:
    def test_int_between(self):
        result = RandomUtils.int_between(1, 10)
        assert 1 <= result <= 10

    def test_float_between(self):
        result = RandomUtils.float_between(1.0, 10.0)
        assert 1.0 <= result <= 10.0

    def test_choice(self):
        result = RandomUtils.choice([1, 2, 3])
        assert result in [1, 2, 3]

    def test_report(self):
        r = RandomUtils.report("int_between", 5)
        assert r.operation == "int_between"
        assert r.value == 5
        assert r.timestamp
