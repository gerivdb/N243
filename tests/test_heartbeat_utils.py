#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du heartbeat_utils.py
"""

from agents.heartbeat_utils import HeartbeatUtils


class TestHeartbeatUtils:
    def test_check(self):
        utils = HeartbeatUtils()
        report = utils.check({"alive": True})
        assert report.alive is True
