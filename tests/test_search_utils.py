#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du search_utils.py
"""

from agents.search_utils import SearchUtils, SearchReport


class TestSearchUtils:
    def test_find(self):
        result = SearchUtils.find([1, 2, 3], lambda x: x >= 2)
        assert result == 2

    def test_find_default(self):
        result = SearchUtils.find([1, 2, 3], lambda x: x >= 10, "not_found")
        assert result == "not_found"

    def test_find_all(self):
        result = SearchUtils.find_all([1, 2, 3, 4], lambda x: x >= 2)
        assert result == [2, 3, 4]

    def test_contains(self):
        assert SearchUtils.contains([1, 2, 3], lambda x: x == 2) is True
        assert SearchUtils.contains([1, 2, 3], lambda x: x == 10) is False

    def test_report(self):
        r = SearchUtils.report("find", 2)
        assert r.operation == "find"
        assert r.found == 2
        assert r.timestamp
