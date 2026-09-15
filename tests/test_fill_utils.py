#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du fill_utils.py
"""

from agents.fill_utils import FillUtils


class TestFillUtils:
    def test_apply(self):
        utils = FillUtils()
        report = utils.apply([1, 2, 3, 4], start=1, end=3, fill=0)
        assert report.filled == [1, 0, 0, 4]
