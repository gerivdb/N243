#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du integrator_utils.py
"""

from agents.integrator_utils import IntegratorUtils


class TestIntegratorUtils:
    def test_cumulative_sum(self):
        utils = IntegratorUtils()
        assert utils.cumulative_sum([1.0, 2.0, 3.0]) == [1.0, 3.0, 6.0]

    def test_report(self):
        utils = IntegratorUtils()
        report = utils.report([1.0, 2.0, 3.0])
        assert report.total == 3.0
