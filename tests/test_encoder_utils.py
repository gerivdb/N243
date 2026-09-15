#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du encoder_utils.py
"""

from agents.encoder_utils import EncoderUtils


class TestEncoderUtils:
    def test_encode_base64(self):
        utils = EncoderUtils()
        assert utils.encode_base64("abc") == "YWJj"

    def test_report(self):
        utils = EncoderUtils()
        report = utils.report("abc", "YWJj")
        assert report.original_length == 3
        assert report.encoded_length == 4
