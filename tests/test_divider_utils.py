#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du divider_utils.py
"""

from agents.divider_utils import DividerUtils


class TestDividerUtils:
    def test_divide(self):
        utils = DividerUtils()
        assert utils.divide(10, 2) == 5.0

    def test_divide_by_zero(self):
        utils = DividerUtils()
        assert utils.divide(10, 0, default=0) == 0

    def test_report(self):
        utils = DividerUtils()
        report = utils.report(10, 2, True, 5.0)
        assert report.result == 5.0
        assert report.success is True
