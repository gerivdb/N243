#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du sorter_utils.py
"""

from agents.sorter_utils import SorterUtils, SorterReport


class TestSorterUtils:
    def test_sort_asc(self):
        assert SorterUtils.sort_asc([3, 1, 2]) == [1, 2, 3]

    def test_sort_desc(self):
        assert SorterUtils.sort_desc([1, 3, 2]) == [3, 2, 1]

    def test_sort_by(self):
        result = SorterUtils.sort_by([{"x": 2}, {"x": 1}], key=lambda d: d["x"])
        assert result == [{"x": 1}, {"x": 2}]

    def test_report(self):
        r = SorterUtils.report("sort_asc", [1, 2, 3])
        assert r.operation == "sort_asc"
        assert r.result == [1, 2, 3]
        assert r.timestamp
