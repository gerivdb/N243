#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du reducer_utils.py
"""

from agents.reducer_utils import ReducerUtils


class TestReducerUtils:
    def test_reduce_sum(self):
        utils = ReducerUtils()
        assert utils.reduce([1, 2, 3], lambda a, b: a + b) == 6

    def test_reduce_with_initial(self):
        utils = ReducerUtils()
        assert utils.reduce([1, 2, 3], lambda a, b: a + b, 10) == 16

    def test_report(self):
        utils = ReducerUtils()
        report = utils.report("sum", 6)
        assert report.operator == "sum"
        assert report.result == 6
