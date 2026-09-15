#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du partition_utils.py
"""

from agents.partition_utils import PartitionUtils


class TestPartitionUtils:
    def test_apply(self):
        utils = PartitionUtils()
        report = utils.apply([0, 1, False, True, 2])
        assert report.truthy == [1, True, 2]
        assert report.falsy == [0, False]
