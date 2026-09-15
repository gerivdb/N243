#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du interpolator_utils.py
"""

from agents.interpolator_utils import InterpolatorUtils


class TestInterpolatorUtils:
    def test_linear(self):
        utils = InterpolatorUtils()
        assert utils.linear([(0.0, 0.0), (2.0, 4.0)], 1.0) == 2.0

    def test_report(self):
        utils = InterpolatorUtils()
        report = utils.report([(0.0, 0.0), (2.0, 4.0)], 1.0)
        assert report.y == 2.0
