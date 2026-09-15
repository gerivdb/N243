#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du failover_utils.py
"""

from agents.failover_utils import FailoverUtils


class TestFailoverUtils:
    def test_primary_alive(self):
        utils = FailoverUtils()
        report = utils.select([{"name": "a", "alive": True}, {"name": "b", "alive": True}], primary="a")
        assert report.active == "a"

    def test_fallback(self):
        utils = FailoverUtils()
        report = utils.select([{"name": "a", "alive": False}, {"name": "b", "alive": True}], primary="a")
        assert report.active == "b"
