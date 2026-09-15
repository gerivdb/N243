#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du padder_utils.py
"""

from agents.padder_utils import PadderUtils


class TestPadderUtils:
    def test_pad_left(self):
        utils = PadderUtils()
        assert utils.pad("abc", 5) == "abc  "

    def test_pad_right(self):
        utils = PadderUtils()
        assert utils.pad("abc", 5, align="right") == "  abc"

    def test_report(self):
        utils = PadderUtils()
        report = utils.report("abc", "abc  ")
        assert report.original_length == 3
        assert report.padded_length == 5
