#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du regexer_utils.py
"""

from agents.regexer_utils import RegexerUtils


class TestRegexerUtils:
    def test_search(self):
        utils = RegexerUtils()
        assert utils.search(r"\d+", "abc123def456") == ["123", "456"]

    def test_report(self):
        utils = RegexerUtils()
        report = utils.report(r"\d+", ["123", "456"])
        assert report.matches == 2
