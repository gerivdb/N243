#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du slice_utils.py
"""

from agents.slice_utils import SliceUtils


class TestSliceUtils:
    def test_slice_list(self):
        utils = SliceUtils()
        assert utils.slice_list([1, 2, 3, 4], 1, 3) == [2, 3]

    def test_slice_str(self):
        utils = SliceUtils()
        assert utils.slice_str("abcdef", 0, 3) == "abc"

    def test_report(self):
        utils = SliceUtils()
        result = utils.report("list", slice(0, 2), [1, 2])
        assert result.source_type == "list"
        assert result.result == [1, 2]
