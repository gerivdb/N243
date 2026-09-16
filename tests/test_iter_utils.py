#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du iter_utils.py
"""

from agents.iter_utils import IterUtils, IterReport


class TestIterUtils:
    def test_take(self):
        result = IterUtils.take([1, 2, 3, 4, 5], 3)
        assert result == [1, 2, 3]

    def test_skip(self):
        result = IterUtils.skip([1, 2, 3, 4, 5], 2)
        assert result == [3, 4, 5]

    def test_chunk(self):
        result = IterUtils.chunk([1, 2, 3, 4, 5], 2)
        assert result == [[1, 2], [3, 4], [5]]

    def test_report(self):
        r = IterUtils.report("take", [1, 2])
        assert r.operation == "take"
        assert r.result == [1, 2]
        assert r.timestamp
