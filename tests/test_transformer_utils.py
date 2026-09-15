#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du transformer_utils.py
"""

from agents.transformer_utils import TransformerUtils


class TestTransformerUtils:
    def test_map_items(self):
        utils = TransformerUtils()
        assert utils.map_items([1, 2, 3], lambda x: x * 2) == [2, 4, 6]

    def test_filter_items(self):
        utils = TransformerUtils()
        assert utils.filter_items([1, 2, 3, 4], lambda x: x % 2 == 0) == [2, 4]

    def test_report(self):
        utils = TransformerUtils()
        result = utils.report("map", 3, 3, [2, 4, 6])
        assert result.operation == "map"
        assert result.output_count == 3
