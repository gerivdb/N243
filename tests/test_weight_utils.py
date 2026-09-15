#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du weight_utils.py
"""

from agents.weight_utils import WeightUtils


class TestWeightUtils:
    def test_apply(self):
        utils = WeightUtils()
        assert utils.apply([1.0, 2.0], [0.5, 0.5]) == [0.5, 1.0]

    def test_report(self):
        utils = WeightUtils()
        report = utils.report([1.0, 2.0], [0.5, 0.5])
        assert report.weighted_sum == 1.5
