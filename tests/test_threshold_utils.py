#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du threshold_utils.py
"""

from agents.threshold_utils import ThresholdUtils, ThresholdReport


class TestThresholdUtils:
    def test_exceeds(self):
        assert ThresholdUtils.exceeds(10, 5) is True
        assert ThresholdUtils.exceeds(3, 5) is False

    def test_below(self):
        assert ThresholdUtils.below(3, 5) is True
        assert ThresholdUtils.below(10, 5) is False

    def test_in_range(self):
        assert ThresholdUtils.in_range(5, 0, 10) is True
        assert ThresholdUtils.in_range(15, 0, 10) is False

    def test_evaluate(self):
        assert ThresholdUtils.evaluate(5, {"min": 0, "max": 10}) == "ok"
        assert ThresholdUtils.evaluate(-5, {"min": 0, "max": 10}) == "below_min"
        assert ThresholdUtils.evaluate(15, {"min": 0, "max": 10}) == "above_max"

    def test_report(self):
        r = ThresholdUtils.report(5, {"min": 0, "max": 10})
        assert r.value == 5
        assert r.status == "ok"
        assert r.timestamp
