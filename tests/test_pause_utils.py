#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du pause_utils.py
"""

from agents.pause_utils import PauseUtils


class TestPauseUtils:
    def test_filter(self):
        utils = PauseUtils()
        report = utils.filter([{"value": 1, "paused": True}, {"value": 2, "paused": False}])
        assert report.paused == [1]
