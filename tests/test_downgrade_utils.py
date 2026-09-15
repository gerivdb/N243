#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du downgrade_utils.py
"""

from agents.downgrade_utils import DowngradeUtils


class TestDowngradeUtils:
    def test_filter(self):
        utils = DowngradeUtils()
        report = utils.filter([{"value": 1, "downgrade": True}, {"value": 2, "downgrade": False}])
        assert report.downgraded == [1]
