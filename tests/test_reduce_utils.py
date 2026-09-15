#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du reduce_utils.py
"""

from agents.reduce_utils import ReduceUtils


class TestReduceUtils:
    def test_apply(self):
        utils = ReduceUtils()
        report = utils.apply([1, 2, 3], func=lambda acc, value: acc + value, initial=0)
        assert report.reduced == 6
