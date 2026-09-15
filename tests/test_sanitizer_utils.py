#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du sanitizer_utils.py
"""

from agents.sanitizer_utils import SanitizerUtils


class TestSanitizerUtils:
    def test_remove_chars(self):
        utils = SanitizerUtils()
        assert utils.remove_chars("a,b;c", [",", ";"]) == "abc"

    def test_report(self):
        utils = SanitizerUtils()
        report = utils.report("a,b", "ab", 1)
        assert report.removed == 1
        assert report.sanitized == "ab"
