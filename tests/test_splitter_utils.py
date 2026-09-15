#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du splitter_utils.py
"""

from agents.splitter_utils import SplitterUtils


class TestSplitterUtils:
    def test_split(self):
        utils = SplitterUtils()
        assert utils.split("a,b,c", ",") == ["a", "b", "c"]

    def test_split_empty(self):
        utils = SplitterUtils()
        assert utils.split("", ",") == []

    def test_report(self):
        utils = SplitterUtils()
        report = utils.report(",", ["a", "b"])
        assert report.parts == 2
        assert report.items == ["a", "b"]
