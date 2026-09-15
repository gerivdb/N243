#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du hold_utils.py
"""

from agents.hold_utils import HoldUtils


class TestHoldUtils:
    def test_filter(self):
        utils = HoldUtils()
        report = utils.filter([1.0, 5.0, 3.0], threshold=3.0)
        assert report.held == [5.0, 3.0]
