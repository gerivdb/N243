#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du recovery_utils.py
"""

from agents.recovery_utils import RecoveryUtils


class TestRecoveryUtils:
    def test_filter(self):
        utils = RecoveryUtils()
        report = utils.filter([{"value": 1, "recovery": True}, {"value": 2, "recovery": False}])
        assert report.recovered == [1]
