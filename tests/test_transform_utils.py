#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du transform_utils.py
"""

from agents.transform_utils import TransformUtils


class TestTransformUtils:
    def test_map_items(self):
        utils = TransformUtils()
        assert utils.map_items([1, 2, 3], lambda x: x * 2) == [2, 4, 6]

    def test_filter_items(self):
        utils = TransformUtils()
        assert utils.filter_items([1, 2, 3, 4], lambda x: x % 2 == 0) == [2, 4]

    def test_reduce_items_sum(self):
        utils = TransformUtils()
        assert utils.reduce_items([1, 2, 3, 4], lambda a, b: a + b, 0) == 10

    def test_reduce_items_product(self):
        utils = TransformUtils()
        assert utils.reduce_items([1, 2, 3, 4], lambda a, b: a * b, 1) == 24

    def test_report(self):
        utils = TransformUtils()
        result = utils.report("map", 3, 3, [2, 4, 6])
        assert result.operation == "map"
        assert result.output_count == 3
