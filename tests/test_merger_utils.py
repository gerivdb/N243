#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du merger_utils.py
"""

from agents.merger_utils import MergerUtils


class TestMergerUtils:
    def test_merge_dicts(self):
        utils = MergerUtils()
        result = utils.merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
        assert result == {"a": 1, "b": 3, "c": 4}

    def test_report(self):
        utils = MergerUtils()
        report = utils.report([{"a": 1}, {"b": 2}])
        assert report.sources == 2
        assert report.keys == ["a", "b"]
