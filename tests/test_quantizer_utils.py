#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du quantizer_utils.py
"""

from agents.quantizer_utils import QuantizerUtils


class TestQuantizerUtils:
    def test_quantize(self):
        utils = QuantizerUtils()
        assert utils.quantize([1.234, 5.678]) == [1.23, 5.68]

    def test_report(self):
        utils = QuantizerUtils()
        report = utils.report([1.234, 5.678])
        assert report.quantized == [1.23, 5.68]
