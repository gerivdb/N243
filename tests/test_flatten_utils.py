#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du flatten_utils.py
"""

from agents.flatten_utils import FlattenUtils


class TestFlattenUtils:
    def test_apply(self):
        utils = FlattenUtils()
        report = utils.apply([1, [2, 3], 4])
        assert report.flat == [1, 2, 3, 4]
