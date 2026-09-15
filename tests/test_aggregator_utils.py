#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du aggregator_utils.py
"""

from agents.aggregator_utils import AggregatorUtils


class TestAggregatorUtils:
    def test_sum_values(self):
        utils = AggregatorUtils()
        assert utils.sum_values([1, 2, 3]) == 6.0

    def test_avg(self):
        utils = AggregatorUtils()
        assert utils.avg([1, 2, 3]) == 2.0
        assert utils.avg([]) == 0.0

    def test_min_max(self):
        utils = AggregatorUtils()
        assert utils.min_max([3, 1, 2]) == {"min": 1, "max": 3}
        assert utils.min_max([]) == {"min": 0.0, "max": 0.0}

    def test_report(self):
        utils = AggregatorUtils()
        result = utils.report("sum", [1, 2, 3], 6.0)
        assert result.operation == "sum"
        assert result.result == 6.0
