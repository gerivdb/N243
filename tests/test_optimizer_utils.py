#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du optimizer_utils.py
"""

from agents.optimizer_utils import OptimizerUtils


def quadratic(x: float) -> float:
    return (x - 2) ** 2


class TestOptimizerUtils:
    def test_minimize(self):
        utils = OptimizerUtils()
        report = utils.minimize(quadratic, start=0.0)
        assert report.best_value < 0.1

    def test_report(self):
        utils = OptimizerUtils()
        report = utils.minimize(quadratic, start=0.0)
        assert report.iterations == 10
