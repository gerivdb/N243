#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du lifetime_utils.py
"""

from agents.lifetime_utils import LifetimeUtils


class TestLifetimeUtils:
    def test_initial_state(self):
        utils = LifetimeUtils()
        assert utils.state() == "created"

    def test_set_state(self):
        utils = LifetimeUtils()
        utils.set_state("active")
        assert utils.state() == "active"
        assert utils.history() == ["created", "active"]

    def test_report(self):
        utils = LifetimeUtils()
        utils.set_state("active")
        report = utils.report()
        assert report.state == "active"
        assert report.history == ["created", "active"]
