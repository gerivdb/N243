#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du pool_utils.py
"""

from agents.pool_utils import PoolUtils


class TestPoolUtils:
    def test_group(self):
        utils = PoolUtils()
        groups = utils.group([1, 2, 1, 3], key="self")
        assert groups[1] == [1, 1]

    def test_report(self):
        utils = PoolUtils()
        report = utils.report([1, 2, 1, 3])
        assert report.groups == 3
