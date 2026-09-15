#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du scaler_utils.py
"""

from agents.scaler_utils import ScalerUtils


class TestScalerUtils:
    def test_min_max(self):
        utils = ScalerUtils()
        assert utils.min_max([0.0, 5.0, 10.0]) == [0.0, 0.5, 1.0]

    def test_report(self):
        utils = ScalerUtils()
        report = utils.report([0.0, 5.0, 10.0])
        assert report.scaled == [0.0, 0.5, 1.0]
