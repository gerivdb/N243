#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du verifier_utils.py
"""

import hashlib

from agents.verifier_utils import VerifierUtils


class TestVerifierUtils:
    def test_verify_valid(self):
        utils = VerifierUtils()
        signature = hashlib.sha256("abc:secret".encode()).hexdigest()
        assert utils.verify("abc", "secret", signature) is True

    def test_verify_invalid(self):
        utils = VerifierUtils()
        assert utils.verify("abc", "secret", "bad") is False

    def test_report(self):
        utils = VerifierUtils()
        report = utils.report("sha256", True)
        assert report.valid is True
