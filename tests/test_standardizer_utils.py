#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du standardizer_utils.py
"""

from agents.standardizer_utils import StandardizerUtils


class TestStandardizerUtils:
    def test_z_score(self):
        utils = StandardizerUtils()
        result = utils.z_score([1.0, 2.0, 3.0])
        assert abs(result[1]) < 1e-6

    def test_report(self):
        utils = StandardizerUtils()
        report = utils.report([1.0, 2.0, 3.0])
        assert len(report.standardized) == 3
