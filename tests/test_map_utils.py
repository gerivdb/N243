#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du map_utils.py
"""

from agents.map_utils import MapUtils


class TestMapUtils:
    def test_apply(self):
        utils = MapUtils()
        report = utils.apply([1, 2, 3], func=lambda value: value * 2)
        assert report.mapped == [2, 4, 6]
