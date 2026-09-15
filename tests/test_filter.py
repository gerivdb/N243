#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du filter.py
"""

from agents.filter import Filter


class TestFilter:
    def test_apply(self):
        filt = Filter()
        items = [1, 2, 3, 4]
        matched = filt.apply(items, lambda x: x > 2)
        assert matched == [3, 4]
        report = filt.report()
        assert report["matched"] == 2

    def test_no_match(self):
        filt = Filter()
        items = [1, 2, 3]
        matched = filt.apply(items, lambda x: x > 10)
        assert matched == []
        assert filt.report()["matched"] == 0
