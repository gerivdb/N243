#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du groupby_utils.py
"""

from agents.groupby_utils import GroupByUtils


class TestGroupByUtils:
    def test_apply(self):
        utils = GroupByUtils()
        report = utils.apply([1, 2, 3, 4], key=lambda value: str(value % 2))
        assert report.groups == {"1": [1, 3], "0": [2, 4]}
