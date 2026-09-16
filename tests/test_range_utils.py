#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du range_utils.py
"""

from agents.range_utils import RangeUtils, RangeReport


class TestRangeUtils:
    def test_range_inclusive(self):
        assert RangeUtils.range_inclusive(1, 5) == [1, 2, 3, 4, 5]

    def test_step_range(self):
        assert RangeUtils.step_range(0, 10, 2) == [0, 2, 4, 6, 8, 10]

    def test_chunks(self):
        result = RangeUtils.chunks([1, 2, 3, 4, 5], 2)
        assert result == [[1, 2], [3, 4], [5]]

    def test_chunks_invalid_size(self):
        try:
            RangeUtils.chunks([1, 2, 3], 0)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass

    def test_report(self):
        r = RangeUtils.report("range_inclusive", [1, 2, 3])
        assert r.operation == "range_inclusive"
        assert r.result == [1, 2, 3]
        assert r.timestamp
