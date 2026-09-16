#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du aggregator_utils.py
"""

from agents.aggregator_utils import AggregatorUtils


class TestAggregatorUtils:
    def test_inspect(self):
        utils = AggregatorUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.aggregated == ["a"]
