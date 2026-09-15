#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du extrapolator_utils.py
"""

from agents.extrapolator_utils import ExtrapolatorUtils


class TestExtrapolatorUtils:
    def test_extrapolate(self):
        utils = ExtrapolatorUtils()
        assert utils.extrapolate([1.0, 2.0, 3.0], steps=1) == 4.0

    def test_report(self):
        utils = ExtrapolatorUtils()
        report = utils.report([1.0, 2.0, 3.0], steps=1)
        assert report.last == 3.0
        assert report.extrapolated == 4.0
