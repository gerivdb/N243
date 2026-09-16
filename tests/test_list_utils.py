#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du list_utils.py
"""

from agents.list_utils import ListUtils, ListReport


class TestListUtils:
    def test_unique(self):
        result = ListUtils.unique([1, 2, 2, 3, 3, 3])
        assert result == [1, 2, 3]

    def test_flatten(self):
        result = ListUtils.flatten([[1, 2], [3, 4]])
        assert result == [1, 2, 3, 4]

    def test_chunk(self):
        result = ListUtils.chunk([1, 2, 3, 4, 5], 2)
        assert result == [[1, 2], [3, 4], [5]]

    def test_report(self):
        r = ListUtils.report("unique", [1, 2, 3])
        assert r.operation == "unique"
        assert r.result == [1, 2, 3]
        assert r.timestamp
