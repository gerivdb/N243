#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du analyzer_utils.py
"""

from agents.analyzer_utils import AnalyzerUtils


class TestAnalyzerUtils:
    def test_stats(self):
        utils = AnalyzerUtils()
        report = utils.stats("hello world")
        assert report.length == 11
        assert report.words == 2
