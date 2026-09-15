#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du timer_utils.py
"""

from agents.timer_utils import TimerUtils


class TestTimerUtils:
    def test_measure(self):
        utils = TimerUtils()
        report = utils.measure([1.0, 2.0, 3.0])
        assert report.elapsed >= 0.0
