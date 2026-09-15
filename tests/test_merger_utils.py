#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du merger_utils.py
"""

from agents.merger_utils import MergerUtils


class TestMergerUtils:
    def test_merge(self):
        utils = MergerUtils()
        base = {"a": 1, "b": 2}
        override = {"b": 3, "c": 4}
        result = utils.merge(base, override)
        assert result == {"a": 1, "b": 3, "c": 4}

    def test_report(self):
        utils = MergerUtils()
        report = utils.report({"a": 1}, {"a": 2, "b": 3})
        assert report.keys_added == 1
        assert report.keys_overwritten == 1
