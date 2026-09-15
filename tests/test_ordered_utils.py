#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du ordered_utils.py
"""

from agents.ordered_utils import OrderedUtils


class TestOrderedUtils:
    def test_sort_unique(self):
        utils = OrderedUtils()
        assert utils.sort_unique([3, 1, 2, 1]) == [1, 2, 3]

    def test_reverse(self):
        utils = OrderedUtils()
        assert utils.reverse([1, 2, 3]) == [3, 2, 1]

    def test_report(self):
        utils = OrderedUtils()
        result = utils.report("sort_unique", 4, 3, [1, 2, 3])
        assert result.operation == "sort_unique"
        assert result.output_count == 3
