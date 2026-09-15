#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du signer_utils.py
"""

from agents.signer_utils import SignerUtils


class TestSignerUtils:
    def test_sign(self):
        utils = SignerUtils()
        assert len(utils.sign("abc", "secret")) == 64

    def test_report(self):
        utils = SignerUtils()
        report = utils.report("sha256", "abc123")
        assert report.algorithm == "sha256"
        assert report.signature == "abc123"
