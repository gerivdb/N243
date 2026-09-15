#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du sort_utils.py
"""

from agents.sort_utils import SortUtils


class TestSortUtils:
    def test_apply(self):
        utils = SortUtils()
        report = utils.apply([3, 1, 2])
        assert report.sorted == [1, 2, 3]
