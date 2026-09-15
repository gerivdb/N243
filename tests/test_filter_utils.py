#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du filter_utils.py
"""

from agents.filter_utils import FilterUtils


class TestFilterUtils:
    def test_include(self):
        utils = FilterUtils()
        assert utils.include([1, 2, 3, 4], lambda x: x % 2 == 0) == [2, 4]

    def test_exclude(self):
        utils = FilterUtils()
        assert utils.exclude([1, 2, 3, 4], lambda x: x % 2 == 0) == [1, 3]

    def test_report(self):
        utils = FilterUtils()
        result = utils.report("include", 4, 2, [2, 4])
        assert result.operation == "include"
        assert result.output_count == 2
