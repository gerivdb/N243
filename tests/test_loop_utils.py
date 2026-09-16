#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du loop_utils.py
"""

from agents.loop_utils import LoopUtils, LoopReport


class TestLoopUtils:
    def test_chunk(self):
        result = LoopUtils.chunk([1, 2, 3, 4, 5], 2)
        assert result == [[1, 2], [3, 4], [5]]

    def test_batch_map(self):
        result = LoopUtils.batch_map([1, 2, 3], lambda x: x * 2)
        assert result == [2, 4, 6]

    def test_find_first(self):
        result = LoopUtils.find_first([1, 2, 3], lambda x: x >= 2)
        assert result == 2

    def test_find_first_default(self):
        result = LoopUtils.find_first([1, 2, 3], lambda x: x >= 10, "not_found")
        assert result == "not_found"

    def test_report(self):
        r = LoopUtils.report("batch_map", [1, 2])
        assert r.operation == "batch_map"
        assert r.result == [1, 2]
        assert r.timestamp
