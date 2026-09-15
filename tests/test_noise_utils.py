#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du noise_utils.py
"""

from agents.noise_utils import NoiseUtils


class TestNoiseUtils:
    def test_generate(self):
        utils = NoiseUtils()
        samples = utils.generate(count=4)
        assert len(samples) == 4
        assert all(0.0 <= value <= 1.0 for value in samples)

    def test_report(self):
        utils = NoiseUtils()
        report = utils.report(count=4)
        assert report.count == 4
