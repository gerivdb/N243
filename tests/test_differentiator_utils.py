#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du differentiator_utils.py
"""

from agents.differentiator_utils import DifferentiatorUtils


class TestDifferentiatorUtils:
    def test_diff(self):
        utils = DifferentiatorUtils()
        assert utils.diff([1.0, 3.0, 6.0]) == [2.0, 3.0]

    def test_report(self):
        utils = DifferentiatorUtils()
        report = utils.report([1.0, 3.0, 6.0])
        assert report.diffs == [2.0, 3.0]
