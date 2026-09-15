#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du accumulator_utils.py
"""

from agents.accumulator_utils import AccumulatorUtils


class TestAccumulatorUtils:
    def test_add(self):
        acc = AccumulatorUtils()
        acc.add(1)
        acc.add(2)
        assert acc.total() == 3
        assert acc.count() == 2

    def test_report(self):
        acc = AccumulatorUtils()
        acc.add(1)
        report = acc.report()
        assert report.count == 1
        assert report.total == 1
