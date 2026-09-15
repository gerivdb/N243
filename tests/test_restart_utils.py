#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du restart_utils.py
"""

from agents.restart_utils import RestartUtils


class TestRestartUtils:
    def test_filter(self):
        utils = RestartUtils()
        report = utils.filter([{"value": 1, "restart": True}, {"value": 2, "restart": False}])
        assert report.restarted == [1]
