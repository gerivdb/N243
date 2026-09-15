#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du merge_utils.py
"""

from agents.merge_utils import MergeUtils


class TestMergeUtils:
    def test_apply(self):
        utils = MergeUtils()
        report = utils.apply([1, 2], [2, 3])
        assert report.merged == [1, 2, 3]
