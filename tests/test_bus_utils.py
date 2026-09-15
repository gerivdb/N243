#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du bus_utils.py
"""

from agents.bus_utils import BusUtils


class TestBusUtils:
    def test_inspect(self):
        utils = BusUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.routed == ["a"]
