#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du ungroup_utils.py
"""

from agents.ungroup_utils import UngroupUtils


class TestUngroupUtils:
    def test_ungroup(self):
        utils = UngroupUtils()
        groups = {"a": [1, 2], "b": [3]}
        assert utils.ungroup(groups) == [1, 2, 3]

    def test_report(self):
        utils = UngroupUtils()
        report = utils.report({"a": [1], "b": [2]})
        assert report.groups == 2
        assert report.items == [1, 2]
