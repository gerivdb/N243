#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du rollback_utils.py
"""

from agents.rollback_utils import RollbackUtils


class TestRollbackUtils:
    def test_filter(self):
        utils = RollbackUtils()
        report = utils.filter([{"value": 1, "rollback": True}, {"value": 2, "rollback": False}])
        assert report.rolled_back == [1]
