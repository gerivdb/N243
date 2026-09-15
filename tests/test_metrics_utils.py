#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du metrics_utils.py
"""

from agents.metrics_utils import MetricsUtils


class TestMetricsUtils:
    def test_collect(self):
        utils = MetricsUtils()
        report = utils.collect(["cpu", "mem"], {"cpu": 1, "mem": None})
        assert report.collected == ["cpu"]
