#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du timer.py
"""

from agents.timer import Timer


class TestTimer:
    def test_mark(self):
        timer = Timer()
        b1 = timer.mark("step-1")
        b2 = timer.mark("step-2")
        assert b1.elapsed_sec <= b2.elapsed_sec
        report = timer.report()
        assert report["total_marks"] == 2

    def test_report_empty(self):
        timer = Timer()
        report = timer.report()
        assert report["total_marks"] == 0
        assert report["last_elapsed_sec"] == 0.0
