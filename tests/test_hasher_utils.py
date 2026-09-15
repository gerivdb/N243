#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du hasher_utils.py
"""

from agents.hasher_utils import HasherUtils


class TestHasherUtils:
    def test_sha256(self):
        utils = HasherUtils()
        assert len(utils.sha256("abc")) == 64

    def test_report(self):
        utils = HasherUtils()
        report = utils.report("sha256", "abc123")
        assert report.algorithm == "sha256"
        assert report.digest == "abc123"
