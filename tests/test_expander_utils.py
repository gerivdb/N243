#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du expander_utils.py
"""

from agents.expander_utils import ExpanderUtils


class TestExpanderUtils:
    def test_expand_list(self):
        utils = ExpanderUtils()
        assert utils.expand_list([1, 2], 2) == [1, 1, 2, 2]

    def test_report(self):
        utils = ExpanderUtils()
        report = utils.report([1, 2], [1, 1, 2, 2])
        assert report.expanded == [1, 1, 2, 2]
        assert report.original == [1, 2]
