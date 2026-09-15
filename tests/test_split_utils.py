#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du split_utils.py
"""

from agents.split_utils import SplitUtils


class TestSplitUtils:
    def test_apply(self):
        utils = SplitUtils()
        report = utils.apply([1, 2, 3, 4], index=2)
        assert report.left == [1, 2]
        assert report.right == [3, 4]
