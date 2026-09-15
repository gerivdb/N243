#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du trimmer_utils.py
"""

from agents.trimmer_utils import TrimmerUtils


class TestTrimmerUtils:
    def test_trim(self):
        utils = TrimmerUtils()
        assert utils.trim("abcdef", 3) == "..."
        assert utils.trim("abc", 5) == "abc"

    def test_report(self):
        utils = TrimmerUtils()
        report = utils.report("abcdef", "abc...")
        assert report.original_length == 6
        assert report.trimmed_length == 6
