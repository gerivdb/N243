#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du scheduler_utils.py
"""

from agents.scheduler_utils import SchedulerUtils


class TestSchedulerUtils:
    def test_schedule_and_run(self):
        scheduler = SchedulerUtils()
        scheduler.schedule("task1", lambda: 42)
        assert scheduler.run("task1") == 42

    def test_cancel(self):
        scheduler = SchedulerUtils()
        scheduler.schedule("task1", lambda: 1)
        scheduler.cancel("task1")
        assert scheduler.report("task1") is None

    def test_report(self):
        scheduler = SchedulerUtils()
        scheduler.schedule("task1", lambda: "ok")
        scheduler.run("task1")
        report = scheduler.report("task1")
        assert report is not None
        assert report.executed is True
        assert report.result == "ok"
