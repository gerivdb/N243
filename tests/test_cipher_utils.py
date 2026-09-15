#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du cipher_utils.py
"""

from agents.cipher_utils import CipherUtils


class TestCipherUtils:
    def test_caesar(self):
        utils = CipherUtils()
        assert utils.caesar("abc", 1) == "bcd"

    def test_report(self):
        utils = CipherUtils()
        report = utils.report("caesar", "bcd")
        assert report.algorithm == "caesar"
        assert report.encrypted == "bcd"
