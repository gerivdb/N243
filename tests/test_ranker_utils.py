#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du ranker_utils.py
"""

from agents.ranker_utils import RankerUtils


class TestRankerUtils:
    def test_rank(self):
        utils = RankerUtils()
        assert utils.rank([3, 1, 2], top_n=2) == [1, 2]

    def test_report(self):
        utils = RankerUtils()
        report = utils.report([3, 1, 2], top_n=2)
        assert report.count == 2
