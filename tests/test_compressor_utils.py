#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du compressor_utils.py
"""

from agents.compressor_utils import CompressorUtils


class TestCompressorUtils:
    def test_compress(self):
        utils = CompressorUtils()
        assert utils.compress("a   b\tc") == "a b c"

    def test_report(self):
        utils = CompressorUtils()
        report = utils.report("a   b", "a b")
        assert report.original_length == 5
        assert report.compressed_length == 3
