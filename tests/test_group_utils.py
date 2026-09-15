#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du group_utils.py
"""

from agents.group_utils import GroupUtils


class TestGroupUtils:
    def test_group_by_key(self):
        utils = GroupUtils()
        items = [
            {"type": "a", "value": 1},
            {"type": "b", "value": 2},
            {"type": "a", "value": 3},
        ]
        grouped = utils.group_by_key(items, "type")
        assert grouped["a"] == [{"type": "a", "value": 1}, {"type": "a", "value": 3}]

    def test_report(self):
        utils = GroupUtils()
        report = utils.report({"a": [1], "b": [2]})
        assert report.groups == 2
        assert "a" in report.keys
