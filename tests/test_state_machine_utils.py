#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du state_machine_utils.py
"""

from agents.state_machine_utils import StateMachineUtils


class TestStateMachineUtils:
    def test_transit_allowed(self):
        sm = StateMachineUtils("idle", ["idle", "running", "done"])
        assert sm.transit("running") is True
        assert sm.state() == "running"

    def test_transit_not_allowed(self):
        sm = StateMachineUtils("idle", ["idle", "running", "done"])
        assert sm.transit("paused") is False
        assert sm.state() == "idle"

    def test_report(self):
        sm = StateMachineUtils("idle", ["idle", "running", "done"])
        sm.transit("running")
        report = sm.report()
        assert report.current == "running"
        assert report.previous == "idle"
