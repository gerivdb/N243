#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du watchdog_utils.py
"""

from agents.watchdog_utils import WatchdogUtils


class TestWatchdogUtils:
    def test_check(self):
        utils = WatchdogUtils()
        report = utils.check([{"alive": True}, {"alive": False}])
        assert report.alive == 1
