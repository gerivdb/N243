#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du collector_utils.py
"""

from agents.collector_utils import CollectorUtils


class TestCollectorUtils:
    def test_inspect(self):
        utils = CollectorUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.collected == ["a"]
