#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du replace_utils.py
"""

from agents.replace_utils import ReplaceUtils


class TestReplaceUtils:
    def test_apply(self):
        utils = ReplaceUtils()
        report = utils.apply([1, 2, 3], target=2, replacement=9)
        assert report.replaced == [1, 9, 3]
