#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du decoder_utils.py
"""

from agents.decoder_utils import DecoderUtils


class TestDecoderUtils:
    def test_decode_base64(self):
        utils = DecoderUtils()
        assert utils.decode_base64("YWJj") == "abc"

    def test_report(self):
        utils = DecoderUtils()
        report = utils.report("YWJj", "abc")
        assert report.original_length == 4
        assert report.decoded_length == 3
