#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du selector_utils.py
"""

from agents.selector_utils import SelectorUtils


class TestSelectorUtils:
    def test_select(self):
        utils = SelectorUtils()
        assert utils.select([1, 2, 3, 4], lambda x: x > 2) == [3, 4]

    def test_report(self):
        utils = SelectorUtils()
        report = utils.report([1, 2])
        assert report.selected == 2
        assert report.items == [1, 2]
