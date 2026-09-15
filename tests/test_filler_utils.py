#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du filler_utils.py
"""

from agents.filler_utils import FillerUtils


class TestFillerUtils:
    def test_fill_dict(self):
        utils = FillerUtils()
        assert utils.fill_dict({"a": 1}, ["a", "b"], 0) == {"a": 1, "b": 0}

    def test_report(self):
        utils = FillerUtils()
        report = utils.report(2)
        assert report.filled == 2
