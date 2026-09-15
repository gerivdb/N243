#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du masker_utils.py
"""

from agents.masker_utils import MaskerUtils


class TestMaskerUtils:
    def test_mask(self):
        utils = MaskerUtils()
        assert utils.mask("abc", visible=0) == "***"
        assert utils.mask("abc", visible=1) == "a**"

    def test_report(self):
        utils = MaskerUtils()
        report = utils.report("abc", "a**")
        assert report.original_length == 3
        assert report.masked_length == 3
