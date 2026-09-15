#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du diff_utils.py
"""

from agents.diff_utils import DiffUtils


class TestDiffUtils:
    def test_compare_changed(self):
        utils = DiffUtils()
        diffs = utils.compare({"a": 1}, {"a": 2})
        assert len(diffs) == 1
        assert diffs[0].kind == "changed"

    def test_compare_added_removed(self):
        utils = DiffUtils()
        diffs = utils.compare({"a": 1}, {"b": 2})
        assert len(diffs) == 2
        kinds = {d.kind for d in diffs}
        assert kinds == {"added", "removed"}

    def test_report(self):
        utils = DiffUtils()
        report = utils.report({"a": 1}, {"a": 2})
        assert report["changed"] == 1
