#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du scheduler_utils.py
"""

from agents.scheduler_utils import SchedulerUtils


class TestSchedulerUtils:
    def test_inspect(self):
        utils = SchedulerUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.scheduled == ["a"]
