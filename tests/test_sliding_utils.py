#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du sliding_utils.py
"""

from agents.sliding_utils import SlidingUtils


class TestSlidingUtils:
    def test_apply(self):
        utils = SlidingUtils()
        report = utils.apply([1, 2, 3, 4, 5], size=2, step=2)
        assert report.windows == [[1, 2], [3, 4]]
