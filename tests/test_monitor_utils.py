#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du monitor_utils.py
"""

from agents.monitor_utils import MonitorUtils


class TestMonitorUtils:
    def test_watch(self):
        utils = MonitorUtils()
        report = utils.watch(["cpu", "mem"], {"cpu": 1, "mem": None})
        assert report.monitored == ["cpu"]
