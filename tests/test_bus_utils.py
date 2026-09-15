#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du bus_utils.py
"""

from agents.bus_utils import BusUtils


class TestBusUtils:
    def test_publish(self):
        utils = BusUtils()
        report = utils.publish([{"topic": "a"}, {"topic": "b"}])
        assert report.messages == 2
