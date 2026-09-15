#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du redundancy_utils.py
"""

from agents.redundancy_utils import RedundancyUtils


class TestRedundancyUtils:
    def test_filter(self):
        utils = RedundancyUtils()
        report = utils.filter([{"value": 1, "redundant": True}, {"value": 2, "redundant": False}])
        assert report.redundant == [1]
