#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du slot_utils.py
"""

from agents.slot_utils import SlotUtils


class TestSlotUtils:
    def test_range(self):
        utils = SlotUtils()
        report = utils.range([1, 2, 3, 4], start=1, end=3)
        assert report.slot == [2, 3]
