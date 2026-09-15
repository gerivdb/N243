#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du distinct_utils.py
"""

from agents.distinct_utils import DistinctUtils


class TestDistinctUtils:
    def test_apply(self):
        utils = DistinctUtils()
        report = utils.apply([1, 2, 2, 3])
        assert report.distinct == [1, 2, 3]
