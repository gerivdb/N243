#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du harmonic_utils.py
"""

from agents.harmonic_utils import HarmonicUtils


class TestHarmonicUtils:
    def test_mean(self):
        utils = HarmonicUtils()
        assert abs(utils.mean([1.0, 2.0, 4.0]) - 1.7142857142857142) < 1e-6

    def test_report(self):
        utils = HarmonicUtils()
        report = utils.report([1.0, 2.0, 4.0])
        assert abs(report.harmonic_mean - 1.7142857142857142) < 1e-6
