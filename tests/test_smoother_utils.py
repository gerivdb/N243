#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du smoother_utils.py
"""

from agents.smoother_utils import SmootherUtils


class TestSmootherUtils:
    def test_moving_average(self):
        utils = SmootherUtils()
        assert utils.moving_average([1.0, 2.0, 3.0], window=2) == [1.0, 1.5, 2.5]

    def test_report(self):
        utils = SmootherUtils()
        report = utils.report([1.0, 2.0, 3.0], window=2)
        assert report.smoothed == [1.0, 1.5, 2.5]
