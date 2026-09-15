#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du upgrade_utils.py
"""

from agents.upgrade_utils import UpgradeUtils


class TestUpgradeUtils:
    def test_filter(self):
        utils = UpgradeUtils()
        report = utils.filter([{"value": 1, "upgrade": True}, {"value": 2, "upgrade": False}])
        assert report.upgraded == [1]
