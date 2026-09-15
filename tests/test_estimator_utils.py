#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du estimator_utils.py
"""

from agents.estimator_utils import EstimatorUtils


class TestEstimatorUtils:
    def test_average(self):
        utils = EstimatorUtils(window=3)
        utils.add(1)
        utils.add(2)
        utils.add(3)
        assert utils.average() == 2.0

    def test_report(self):
        utils = EstimatorUtils(window=3)
        utils.add(1)
        utils.add(2)
        report = utils.report()
        assert report.window == 3
        assert report.average == 1.5
