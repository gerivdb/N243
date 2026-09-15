#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du shutdown_utils.py
"""

from agents.shutdown_utils import ShutdownUtils


class TestShutdownUtils:
    def test_filter(self):
        utils = ShutdownUtils()
        report = utils.filter([{"value": 1, "shutdown": True}, {"value": 2, "shutdown": False}])
        assert report.shutdown == [1]
