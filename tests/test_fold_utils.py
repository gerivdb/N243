#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du fold_utils.py
"""

from agents.fold_utils import FoldUtils


class TestFoldUtils:
    def test_apply(self):
        utils = FoldUtils()
        report = utils.apply([1, 2, 3, 4], func=lambda acc, value: acc + value)
        assert report.folded == [10]
