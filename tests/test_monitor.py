#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du monitor.py
"""

from agents.monitor import Monitor


class TestMonitor:
    def test_check_triggered(self):
        monitor = Monitor()
        alert = monitor.check("cpu", "> 0.9", lambda x: x > 0.9, 0.95)
        assert alert.triggered is True

    def test_check_not_triggered(self):
        monitor = Monitor()
        alert = monitor.check("cpu", "> 0.9", lambda x: x > 0.9, 0.5)
        assert alert.triggered is False

    def test_report(self):
        monitor = Monitor()
        monitor.check("cpu", "> 0.9", lambda x: x > 0.9, 0.95)
        monitor.check("ram", "> 0.9", lambda x: x > 0.9, 0.5)
        report = monitor.report()
        assert report["total_checks"] == 2
        assert report["triggered"] == 1
