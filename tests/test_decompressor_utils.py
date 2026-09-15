#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du decompressor_utils.py
"""

from agents.decompressor_utils import DecompressorUtils


class TestDecompressorUtils:
    def test_decompress(self):
        utils = DecompressorUtils()
        assert utils.decompress("a b c") == "a    b    c"

    def test_report(self):
        utils = DecompressorUtils()
        report = utils.report("a b", "a    b")
        assert report.original_length == 3
        assert report.decompressed_length == 6
